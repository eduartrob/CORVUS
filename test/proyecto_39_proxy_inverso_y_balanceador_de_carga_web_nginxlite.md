# PROTOCOLO DE INVESTIGACIÓN: Proxy Inverso y Balanceador de Carga Web (NginxLite)

*   **Línea de Investigación:** Redes / Sistemas
*   **Complejidad de Implementación:** Avanzado

---

### 1. Resumen Ejecutivo
Una aplicación de red de bajo nivel que actúa como intermediario para redireccionar peticiones de clientes a múltiples servidores web en el backend distribuyendo el tráfico.

### 2. Requerimientos de Software
- Enrutamiento inverso de peticiones entrantes basado en reglas de host o ruta.
- Algoritmos de balanceo de carga implementados (Round Robin, Least Connections).
- Verificación activa de la salud de los servidores backend para ignorar los caídos.
- Caché en disco integrada para respuestas estáticas con el fin de optimizar tiempos.
- Soporte para terminación TLS/SSL segura usando OpenSSL.

### 3. Entorno Tecnológico Propuesto
Para llevar a cabo el prototipo, se utilizará: **Rust, tokio, hyper (HTTP library), openssl, config parser**

### 4. Justificación Científica y Técnica
Este proyecto es ideal para desarrolladores con un nivel **Avanzado** que buscan enriquecer su portafolio profesional. Al completarlo, habrás dominado conceptos clave relacionados con **Redes / Sistemas**, implementando arquitecturas modernas y robustas. ¡Es una excelente adición a tu GitHub!

---

### Referencias
- Joyanes Aguilar, L. (2020). Inteligencia artificial y computación cognitiva. Alfaomega.
- Sommerville, I. (2016). Ingeniería de software. Pearson Educación.
- Russell, S., & Norvig, P. (2020). Inteligencia artificial: un enfoque moderno. Pearson.
