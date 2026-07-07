# 🚀 AutoGrader: Corrector Automático de Tareas de Programación - Repositorio Escolar

> **Categoría:** Educación y ambientes de aprendizaje
> **Dificultad:** Intermedio
> **Grupo de Similitud:** Herramientas Educativas

---

## 📖 Descripción General
Herramienta que ejecuta pruebas unitarias automáticamente sobre entregas de código y detecta plagio estructural.

### Estructura Propuesta de Archivos
```
autograder:_/
├── backend/            ← Lógica del servidor
├── frontend/           ← Vistas e interfaz de usuario
├── docs/               ← Diagramas y documentación
└── README.md           ← Ficha del proyecto
```

---

## 🎯 Características Principales
- Entorno de ejecución aislado mediante sandboxing ligero.
- Lector y ejecutor de pruebas con reporte HTML.
- Comparación de árboles de sintaxis abstracta (AST) para plagio.
- Consola web para que el docente asigne rúbricas.
- Integración de feedback instantáneo por consola para alumnos.

---

## 🛠️ Tecnologías Sugeridas
La arquitectura se sustenta en:
`Docker, Python, AST parser, React, PostgreSQL`

---

## 💡 ¿Por qué es una propuesta innovadora?
Es de gran utilidad para docentes de ingeniería y ciencias computacionales, reduciendo drásticamente la carga de revisión.
