# 🧠 Eduart AI — Agente con Identidad Propia

Proyecto de IA personalizada basada en la identidad, personalidad y
patrones de habla de una persona real. Construido 100% en Python,
diseñado para correr en hardware de 8GB RAM.

---

## 🗂️ Estructura del Proyecto

```
eduart_ai/
│
├── core/                        ← MÓDULO 1: Núcleo de identidad
│   ├── identity_core.json       ← Perfil de personalidad (tú)
│   └── identity.py              ← Clase Identity + EmotionalState
│
├── memory/                      ← MÓDULO 2: Memoria (próximo)
│   ├── short_term.py            ← Contexto de conversación actual (RAM)
│   ├── long_term.py             ← Base vectorial ChromaDB
│   └── episodic.py              ← Log de eventos importantes
│
├── language/                    ← MÓDULO 3: Lenguaje (próximo)
│   ├── generator.py             ← Genera texto "como Eduart"
│   ├── style_analyzer.py        ← Analiza chat WhatsApp
│   └── fine_tune_data/          ← Datos de entrenamiento extraídos
│
├── perception/                  ← MÓDULO 4: Visión (futuro)
│   ├── image_classifier.py      ← CNN para reconocer imágenes
│   └── reaction.py              ← Conecta visión con emociones
│
├── environment/                 ← MÓDULO 5: Entorno 2D (futuro)
│   ├── world.py                 ← Espacio 2D con Pygame
│   └── agent_body.py            ← Cuerpo del agente en el mundo
│
├── data/
│   ├── raw/                     ← Chat WhatsApp exportado (.txt)
│   └── processed/               ← Datos procesados listos para usar
│
├── utils/
│   └── logger.py                ← Sistema de logs
│
├── main.py                      ← Punto de entrada principal
└── README.md                    ← Este archivo
```

---

## 🧩 Módulos y Estado

| Módulo | Estado | Descripción |
|--------|--------|-------------|
| `core/identity` | ✅ Listo | Personalidad + emociones simuladas |
| `memory/` | 🔜 Siguiente | Memoria corto/largo plazo |
| `language/` | 🔜 Siguiente | Generación de texto estilo Eduart |
| `perception/` | ⏳ Futuro | Visión por CNN |
| `environment/` | ⏳ Futuro | Entorno 2D Pygame |

---

## 🚀 Cómo ejecutar el núcleo actual

```bash
cd eduart_ai
python core/identity.py
```

---

## 📦 Dependencias (se irán agregando por módulo)

```bash
# Módulo actual (core) — sin dependencias externas aún
python -m pip install numpy

# Módulo memory (próximo)
pip install chromadb sentence-transformers

# Módulo language (próximo)
pip install transformers torch --index-url https://download.pytorch.org/whl/cpu

# Módulo environment (futuro)
pip install pygame
```

---

## 📊 Precisión del perfil

| Fuente | Aporte | Estado |
|--------|--------|--------|
| Respuestas a preguntas | Base de personalidad | ✅ Procesado |
| Chat de WhatsApp | Estilo de habla real | 🔜 Pendiente |
| **Total actual** | **~62%** | — |
| **Total estimado con WhatsApp** | **~90%+** | — |

---

## 🧠 Arquitectura de Emociones

El agente tiene un vector de 7 emociones numéricas (0.0 → 1.0):

- `curiosidad` — qué tan activo está aprendiendo
- `energia` — nivel de activación general  
- `felicidad` — bienestar del momento
- `frustracion` — bloqueos o límites no superados
- `aburrimiento` — falta de estimulación
- `celos` — comparación con otros agentes
- `motivacion` — impulso de hacer cosas

Cada trigger externo modifica estos valores. Si se crea una segunda IA,
el agente detecta la comparación y puede "ponerse celoso" de forma simulada.
