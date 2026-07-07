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


INFORMACIÓN DE LA PROPUESTA No. 4 (propuesta de prioridad media)
NOMBRE DEL PROYECTO
QuantumAlgoPlay: Visualizador Didáctico de Algoritmos Cuánticos de Gran Escala.
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
El verdadero poder de la computación cuántica radica en sus algoritmos (como el algoritmo de Grover para búsquedas no estructuradas o el de Shor para factorización de enteros). Sin embargo, comprender cómo estos algoritmos manipulan las amplitudes para crear interferencia constructiva en las respuestas correctas e interferencia destructiva en las incorrectas es una tarea compleja debido al alto nivel de matemática teórica requerido, desmotivando a los alumnos de ciencias lógicas.

OBJETIVO GENERAL
Diseñar y desarrollar un simulador educativo interactivo que muestre el flujo paso a paso de algoritmos cuánticos célebres, permitiendo a los estudiantes visualizar de qué manera cambian las fases y probabilidades de los estados cuánticos tras cada etapa del proceso algorítmico.

OBJETIVOS ESPECÍFICOS
- Programar simuladores matemáticos específicos de los algoritmos de Deutsch-Jozsa, Grover (búsqueda) y Shor (paso de estimulación de fase) con parámetros de entrada sencillos.
- Desarrollar diagramas de circuitos automáticos que se dibujen e iluminen en tiempo real según el paso del algoritmo que se esté ejecutando.
- Diseñar un módulo de representación gráfica de "Amplitud y Fase" que ilustre cómo el operador de difusión de Grover incrementa la amplitud del estado objetivo (amplificación de amplitud).
- Crear tutoriales estructurados que guíen al estudiante por la fundamentación matemática detrás de la aceleración cuántica frente a algoritmos clásicos.

JUSTIFICACIÓN
Para formar científicos en computación cuántica, se requiere pasar de la teoría a la visualización de datos de flujo algorítmico. QuantumAlgoPlay se justifica porque permite desglosar un algoritmo complejo como la búsqueda de Grover en partes visuales digeribles: la preparación del estado de superposición uniforme, la aplicación del oráculo (que invierte la fase del estado buscado) y la difusión (que refleja sobre la media, amplificando la probabilidad del estado objetivo). Esta deconstrucción visual mitiga la complejidad y acelera la curva de aprendizaje de forma eficiente.

USUARIOS FINALES
- Usuario Estudiante de Ingeniería: Utiliza la aplicación para ver cómo funcionan Grover o Shor con diferentes entradas de datos, analizando la aceleración matemática resultante de forma secuencial.
- Usuario Instructor Académico: Emplea la aplicación para dar explicaciones dinámicas de la superioridad cuántica (Quantum Supremacy) mediante demostraciones en vivo en entornos virtuales de enseñanza.

LISTA DE FUNCIONALIDADES POR TIPO DE USUARIO
Funcionalidades del Usuario Estudiante de Ingeniería:
1. Selector de Algoritmo Base: Menú para elegir entre el algoritmo de Grover, Deutsch-Jozsa o Shor.
2. Controles de Entrada del Oráculo: Formulario simple para elegir qué elemento buscar (en Grover) o qué función evaluar (en Deutsch-Jozsa).
3. Panel de Pasos Animado: Controles de tipo reproductor de medios (Play, Pausa, Siguiente Paso, Paso Anterior) que muestran los circuitos de compuertas y el histograma en cada estado intermedio.
4. Graficador de Fases Vectoriales: Gráfico interactivo que muestra las amplitudes complejas representadas por flechas 2D cuya longitud es la probabilidad y dirección es la fase.

Funcionalidades del Usuario Instructor Académico:
1. Creador de Scripts Rápidos: Consola integrada de comandos lógicos que permite diseñar oráculos avanzados y exportar el flujo para usarlo en evaluaciones estudiantiles.
2. Monitor de Comparación Cuántica vs Clásica: Comparador gráfico interactivo que muestra el número de consultas necesarias para resolver el mismo problema en un entorno de computación clásico frente al cuántico.

LISTA DE TECNOLOGÍAS A APLICAR
- Interfaz del Sistema: Vue.js, Tailwind CSS, Vuex (gestión de estado de pasos).
- Motor Matemático y Renderizado: JavaScript (MathJS, Cómputo vectorial), D3.js (para la gráfica de flechas complejas).
- Documentación Científica: Markdown integrado con MathJax/KaTeX para visualización óptima de fórmulas de Dirac y matrices.

BIBLIOGRAFÍA CONSULTADA
- Russell, S., & Norvig, P. (2020). *Inteligencia artificial: un enfoque moderno*. Pearson.
- Nielsen, M. A., & Chuang, I. L. (2010). *Quantum Computation and Quantum Information*. Cambridge University Press.
- Sommerville, I. (2016). *Ingeniería de software*. Pearson Educación.
