INFORMACIÓN DEL EQUIPO DE TRABAJO
MATRÍCULA
231502
NOMBRE (S)
Mateo Sebastián
APELLIDOS
Gómez Ruiz
GRUPO
A

228491
NOMBRE (S)
Isabella
APELLIDOS
Sánchez Mendoza
GRUPO
B

230114
NOMBRE (S)
Santiago
APELLIDOS
López Vargas
GRUPO
A


INFORMACIÓN DE LA PROPUESTA No. 1 (propuesta principal o con mayor prioridad)
NOMBRE DEL PROYECTO
QuantumCircuitLab: Simulador Visual e Interactivo de Circuitos Cuánticos de N-Qubits.
CATEGORÍA
(marca con una X)
Social


Ciencias naturales
x

Ciencias humanas


Creativos y culturales


Ciencias de la salud


Educación y ambientes de aprendizaje
x

PROBLEMÁTICA
El aprendizaje de la computación cuántica es altamente abstracto y complejo para los estudiantes de ciencias de la computación. Las herramientas existentes en el mercado son o bien librerías puramente matemáticas basadas en código rígido (como Qiskit en consolas), o bien simuladores web muy limitados que no permiten experimentar visualmente con la interferencia de fase y las matrices de probabilidad en tiempo real, lo que dificulta la comprensión de conceptos como superposición y entrelazamiento.

OBJETIVO GENERAL
Desarrollar una aplicación web interactiva que funcione como un laboratorio visual de circuitos cuánticos para N-qubits. El sistema permitirá a los estudiantes arrastrar y soltar compuertas cuánticas (H, X, Y, Z, CNOT, Toffoli) sobre líneas de tiempo de qubits y ver instantáneamente los resultados de la simulación del vector de estado en forma de amplitudes de probabilidad y fases complejas.

OBJETIVOS ESPECÍFICOS
- Motor de Simulación Cuántica Local: Desarrollar un motor matemático ligero en TypeScript que realice cálculos matriciales y operaciones de producto tensorial para simular de forma exacta hasta 10 qubits sin sobrecargar el procesador del navegador.
- Interfaz Gráfica de Arrastre y Soltado (Drag and Drop): Crear un lienzo interactivo en el frontend para colocar, mover y eliminar compuertas cuánticas sobre canales de qubits.
- Visualizador de Amplitudes y Fases en Tiempo Real: Desarrollar gráficos dinámicos que representen el estado del sistema cuántico mostrando tanto la probabilidad de medición (porcentaje) como el ángulo de fase de cada estado base (utilizando vectores de color).
- Módulo de Ejecución Paso a Paso: Implementar controles de reproducción para avanzar el circuito compuerta por compuerta y analizar la evolución del vector de estado en cada etapa del algoritmo cuántico.

JUSTIFICACIÓN
La transición hacia la era cuántica requiere herramientas didácticas de alta fidelidad visual. Actualmente, los estudiantes se frustran al interactuar únicamente con código matricial abstracto. Este proyecto se justifica al proveer una plataforma visual integrada que traduce los formalismos matemáticos de Dirac (notación bra-ket) en componentes interactivos y comprensibles. Al simular localmente en el navegador, se evitan tiempos de espera de colas en computadoras cuánticas reales o servidores externos, permitiendo un aprendizaje inmediato y dinámico.

USUARIOS FINALES
- Usuario Estudiante: Utiliza el lienzo interactivo para armar circuitos cuánticos sencillos, observar cómo cambian las probabilidades de los estados y aprender las reglas de las compuertas cuánticas básicas mediante retos interactivos integrados.
- Usuario Docente: Utiliza la plataforma para preparar clases dinámicas, diseñar circuitos de prueba y exportar diagramas vectoriales de circuitos para utilizarlos en materiales didácticos o evaluaciones.

LISTA DE FUNCIONALIDADES POR TIPO DE USUARIO
Funcionalidades del Usuario Estudiante:
1. Panel de Circuitos Cuánticos: Área interactiva para colocar compuertas y conectar qubits.
2. Histograma de Probabilidad Dinámico: Gráfica que muestra las probabilidades de medir cada combinación de estados.
3. Biblioteca de Compuertas Básicas: Caja de herramientas con compuertas de un qubit y compuertas de control multi-qubit.
4. Módulo de Retos Didácticos: Sección con ejercicios de lógica cuántica donde el alumno debe construir un circuito que resuelva un estado final específico.

Funcionalidades del Usuario Docente:
1. Creador de Retos y Plantillas: Panel administrativo para diseñar circuitos base y dejarlos como tareas para los alumnos.
2. Exportador de Diagramas: Herramienta para descargar el circuito en formatos SVG o LaTeX.
3. Visor de Matrices del Circuito: Vista avanzada que muestra la matriz unitaria total resultante de todo el circuito cuántico armado.

LISTA DE TECNOLOGÍAS A APLICAR
- Frontend y Lógica de Simulación: TypeScript, React, HTML5 Canvas, CSS Modules.
- Gráficas y Renderizado: D3.js (para histogramas y visualización de matrices de densidad), Tailwind CSS.
- Infraestructura y Empaquetado: Vite, GitHub Pages (para despliegue estático del simulador).

BIBLIOGRAFÍA CONSULTADA
- Russell, S., & Norvig, P. (2020). *Inteligencia artificial: un enfoque moderno*. Pearson.
- Nielsen, M. A., & Chuang, I. L. (2010). *Quantum Computation and Quantum Information*. Cambridge University Press.
- García-Peñalvo, F. J. (2021). *Ecosistemas tecnológicos en educación y empresa*. Editorial Reverte.
