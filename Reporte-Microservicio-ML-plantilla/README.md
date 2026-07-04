# Plantilla LaTeX — Reporte Microservicio ML

Plantilla para el hito del **proyecto final** de Minería de datos: microservicio de aprendizaje **no supervisado** con API REST.

## Uso en Overleaf

1. Suba el contenido de esta carpeta como proyecto nuevo (o suba el ZIP).
2. Compilador: **pdfLaTeX**.
3. Archivo principal: `main.tex`.
4. Secuencia recomendada: **pdfLaTeX → BibTeX → pdfLaTeX → pdfLaTeX**.

## Qué debe completar cada equipo

1. Editar `config/metadata.tex` (equipo, algoritmo, URLs, modalidad).
2. Sustituir todos los marcadores `[Completar: ...]` en `sections/` y `tables/`.
3. Colocar figuras en:
   - `figures/arquitectura/` → PNG, SVG y PDF del diagrama
   - `figures/modelos/`, `figures/resultados/`, `figures/pruebas/`, `figures/api/`
4. Actualizar `openapi_swagger/openapi.yaml` y `API.md`.
5. Añadir notebook y código en el repositorio Git (no solo en Overleaf).

## Entregables del hito (recordatorio)

- Repositorio con microservicio funcional
- PDF compilado desde esta plantilla
- Notebook con evidencia de entrenamiento
- Diagrama de arquitectura (PDF, PNG, SVG)
- Documentación API (PDF + MD)
- Colección Postman/Bruno
- Video demostrativo (5–10 min)

## Estructura

```
main.tex
config/          → estilos, portada, metadatos
sections/        → capítulos 01–12 + anexos
tables/          → tablas reutilizables
figures/         → imágenes del equipo
openapi_swagger/ → OpenAPI + API.md
referencias.bib
```

Universidad Politécnica de Chiapas — Minería de datos — 2026.
