# Documentación de la API (Markdown)

Completar este archivo y publicarlo en el repositorio junto con `openapi.yaml`.

## Base URL

`http://localhost:8000`

## Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/api/v1/infer` | Inferencia no supervisada |
| GET | `/api/v1/inferences` | Historial paginado |
| GET | `/api/v1/inferences/{id}` | Detalle de inferencia |
| GET | `/health` | Salud del servicio |

## Ejemplo de inferencia

```json
{
  "records": [
    {"feature_a": 12.5, "feature_b": 0.03}
  ]
}
```

## Errores comunes

- `422`: esquema de entrada inválido
- `500`: error interno del servicio

Exporte este documento a PDF si el entregable lo exige en ambos formatos.
