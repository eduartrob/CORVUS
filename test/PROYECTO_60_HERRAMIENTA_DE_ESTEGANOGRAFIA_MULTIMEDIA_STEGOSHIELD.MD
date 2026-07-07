# Propuesta Académica: Herramienta de Esteganografía en Archivos Multimedia con Cifrado Simétrico (StegoShield)

* **Materia:** Integración de Tecnologías
* **Categoría del Proyecto:** Ciberseguridad / Esteganografía
* **Complejidad Estimada:** Intermedio - Avanzado

---

### Resumen
Una aplicación de seguridad que permite ocultar mensajes de texto o archivos binarios encriptados dentro de archivos portadores de imagen (PNG, BMP) y audio (WAV) sin alterar perceptiblemente la calidad ni la apariencia visual o auditiva del archivo original.

### Módulos a Desarrollar
- Cifrado previo de la información oculta utilizando algoritmos simétricos robustos como AES-256-GCM.
- Inserción de datos utilizando la técnica del Bit Menos Significativo (LSB - Least Significant Bit) en los canales de color RGB de imágenes o en las muestras de audio.
- Sistema de compresión zlib integrado para maximizar el volumen de datos que se pueden ocultar en el archivo portador.
- Comprobación de capacidad de almacenamiento de datos máximos según las dimensiones o duración del archivo portador elegido.
- Interfaz gráfica o de línea de comandos para empaquetar (ocultar) y desempaquetar (extraer) los datos protegidos mediante una clave de paso.

### Stack Tecnológico
Se plantea el uso de las siguientes herramientas: Python, Pillow (PIL para procesamiento de imágenes), PyCryptodome (criptografía), Wave library, Tkinter

### Utilidad y Justificación Académica
Este proyecto es ideal para desarrolladores con un nivel **Intermedio - Avanzado** que buscan enriquecer su portafolio profesional. Al completarlo, habrás dominado conceptos clave relacionados con **Ciberseguridad / Esteganografía**, implementando arquitecturas modernas y robustas. ¡Es una excelente adición a tu GitHub!
