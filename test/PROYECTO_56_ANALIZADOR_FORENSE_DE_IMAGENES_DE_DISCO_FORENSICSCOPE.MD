# Analizador Forense de Imágenes de Disco y Recuperación de Archivos (ForensicScope)

**Categoría:** Seguridad Informática / Informática Forense
**Grupo de Similitud:** Herramientas Forenses
**Nivel de Dificultad:** Avanzado

---

## Descripción del Proyecto
Una herramienta de análisis forense digital capaz de procesar archivos de imágenes de disco crudas (como archivos .dd o .raw), reconstruir la estructura de sistemas de archivos clásicos (como FAT12/16/32) y extraer archivos eliminados mediante técnicas de tallado de archivos (file carving).

---

## Características Principales
- Lectura de sectores y análisis de la Tabla de Particiones MBR e inicio de volumen.
- Reconstrucción en memoria del árbol de directorios leyendo la Tabla de Asignación de Archivos (FAT) y las entradas de directorio.
- Recuperación de archivos marcados como borrados pero cuyos clústeres aún no han sido sobreescritos.
- Módulo de "File Carving" que detecta firmas binarias comunes (headers/trailers) para recuperar imágenes JPG, documentos PDF y archivos ZIP sin metadatos del sistema de archivos.
- Generación automática de reportes de integridad forense con hashes criptográficos MD5 y SHA-256 de los archivos recuperados.

---

## Stack Tecnológico Sugerido
Python, binascii, estructuración de datos binarios estruct (struct module), CLI curses o Tkinter

---

## ¿Por qué elegir este proyecto?
Este proyecto es ideal para desarrolladores con un nivel **Avanzado** que buscan enriquecer su portafolio profesional. Al completarlo, habrás dominado conceptos clave relacionados con **Seguridad Informática / Informática Forense**, implementando arquitecturas modernas y robustas. ¡Es una excelente adición a tu GitHub!
