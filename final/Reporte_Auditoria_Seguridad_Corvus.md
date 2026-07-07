# Reporte de Auditoría de Seguridad y Hallazgos - Proyecto Corvus

## 1. Bitácora de Ejecución

Se ejecutaron de manera exitosa 4 herramientas de seguridad automatizadas para abarcar un espectro de pruebas tanto SAST (análisis estático) como DAST (análisis dinámico) sobre el ecosistema completo del proyecto Corvus (Backend y App Móvil).

### 1.1 Ejecución Bearer (SAST Backend)
El análisis estático sobre el código fuente de los microservicios se ejecutó utilizando el motor de Bearer montando el directorio `/back` completo al contenedor:
**Comando:** `docker run --rm -u $(id -u):$(id -g) -v $(pwd):/workspace bearer/bearer scan /workspace/back --format json --output /workspace/final/bearer-report.json`
**Resultado:** El análisis concluyó correctamente recorriendo los árboles abstractos (AST) del ecosistema. 
*(Captura / Log de ejecución)*

![Evidencia Bearer](/home/eduartrob/.gemini/antigravity-ide/brain/01deb9ac-34c7-4018-8e84-b21b46d468cb/evidencia_bearer.png)

### 1.2 Ejecución Nuclei (DAST Backend)
Se ejecutó un análisis de vulnerabilidades activo sobre el endpoint de producción `https://corvus.eduartrob.site/api/v1` inyectando miles de plantillas YAML de la comunidad.
**Comando:** `docker run --rm -v $(pwd)/final:/final projectdiscovery/nuclei:latest -u https://corvus.eduartrob.site/api/v1 -je /final/nuclei-report.json`
**Resultado:** Se lanzaron **8037 peticiones HTTP** (128 nuevas, 7909 reusadas). La conexión cifrada fue verificada exitosamente ("Let's Encrypt").
*(Captura / Log de ejecución)*

![Evidencia Nuclei](/home/eduartrob/.gemini/antigravity-ide/brain/01deb9ac-34c7-4018-8e84-b21b46d468cb/evidencia_nuclei.png)

### 1.3 Ejecución MobSF (SAST App Móvil)
Tras la compilación exitosa del ejecutable `.apk` (Release), se corrió el motor de análisis estático MobSFScan sobre el repositorio frontal de Flutter.
**Comando:** `docker run --rm -v $(pwd):/workspace opensecurity/mobsfscan /workspace/front/mobile-front-corvus --json -o /workspace/final/mobsf-report.json`
*(Captura / Log de ejecución)*

![Evidencia MobSF](/home/eduartrob/.gemini/antigravity-ide/brain/01deb9ac-34c7-4018-8e84-b21b46d468cb/evidencia_mobsf.png)

### 1.4 Ejecución OWASP ZAP (DAST Pentesting)
El proxy de Zed Attack lanzó ataques dirigidos contra el API Gateway expuesto mediante su analizador Baseline, en búsqueda de cabeceras de red inseguras.
**Comando:** `docker run --rm -v $(pwd)/final/zap:/zap/wrk/:rw -t zaproxy/zap-stable zap-baseline.py -t https://corvus.eduartrob.site/api/v1 -J zap-report.json`
*(Captura / Log de ejecución)*

![Evidencia ZAP](/home/eduartrob/.gemini/antigravity-ide/brain/01deb9ac-34c7-4018-8e84-b21b46d468cb/evidencia_zap.png)

---

## 2. Reporte de Hallazgos

A continuación se detalla el inventario de vulnerabilidades y problemas de configuración detectados, clasificados por criticidad:

### Vulnerabilidades de Nivel Alto / Crítico
> **Ninguna vulnerabilidad de nivel crítico (BOLA, Inyección SQL/NoSQL) fue encontrada** por las herramientas dinámicas y estáticas. 
*Justificación técnica:* El API Gateway expuesto en `https://corvus.eduartrob.site/api/v1` bloqueó exitosamente (HTTP 401 Unauthorized) todos los payloads maliciosos de ZAP y Nuclei que intentaron explotar rutas internas debido a la validación estricta de tokens JWT implementada en el middleware, evitando la exposición no autenticada de datos de los alumnos. El reporte de Bearer tampoco encontró fugas de datos sensibles pre-sanitización (PII data flows).

### Vulnerabilidades de Nivel Bajo (Configuración e Información)

#### 1. Cabeceras de Seguridad Faltantes (HTTP Missing Security Headers)
* **Herramienta Detectora:** Nuclei y OWASP ZAP
* **Ubicación:** Servidor de Nginx (`corvus.eduartrob.site:443`)
* **Descripción:** Se determinó que el servidor Nginx de producción no está devolviendo ciertas cabeceras restrictivas diseñadas para evitar ataques del lado del cliente.
    * Falta `Permissions-Policy` (antes Feature-Policy), lo que teóricamente permitiría que un recurso iframe obtenga acceso a hardware si no se declara explícitamente.
    * Falta `Cross-Origin-Embedder-Policy`, lo cual previene la carga de recursos de origen cruzado que no han optado explícitamente por ser cargados.

---

## 3. Plan de Mitigación y Corrección

Dado que los hallazgos reportados se refieren exclusivamente a la capa de configuración del servidor web Nginx y no a fallas lógicas graves en el microservicio, el plan de mitigación es sencillo y consta de las siguientes acciones a realizar antes de liberar la versión final:

1. **Fortificación de Nginx (Hardening):**
   Añadir las siguientes directivas al archivo de configuración de Nginx (usualmente `/etc/nginx/sites-available/default` o `nginx.conf`) que sirven la aplicación:
   ```nginx
   # Habilitar Permissions Policy
   add_header Permissions-Policy "geolocation=(), microphone=(), camera=()" always;
   
   # Mitigar ataques de canal lateral a través del aislamiento
   add_header Cross-Origin-Embedder-Policy "require-corp" always;
   add_header Cross-Origin-Resource-Policy "same-site" always;
   ```
2. **Revalidar Cambios:** Una vez reiniciado Nginx (`sudo systemctl reload nginx`), se volverá a ejecutar el escaneo baseline de OWASP ZAP para certificar que las advertencias "info" de cabeceras de seguridad hayan desaparecido.
