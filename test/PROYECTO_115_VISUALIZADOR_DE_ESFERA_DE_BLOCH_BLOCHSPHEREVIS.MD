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


INFORMACIÓN DE LA PROPUESTA No. 3 (propuesta de prioridad media)
NOMBRE DEL PROYECTO
BlochSphereVis: Visualizador Interactivo 3D del Estado de Qubits en la Esfera de Bloch.
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
El estado de un qubit se describe mediante amplitudes de probabilidad complejas, lo que resulta extremadamente difícil de conceptualizar espacialmente. La Esfera de Bloch es el estándar geométrico para representar un estado cuántico puro de dos niveles como un punto en la superficie de una esfera unitaria, pero los alumnos suelen tener dificultades para entender cómo las compuertas lógicas cuánticas (como la compuerta de Hadamard o las rotaciones de fase) equivalen a rotaciones espaciales en los ejes X, Y y Z.

OBJETIVO GENERAL
Desarrollar un visualizador tridimensional web interactivo de la Esfera de Bloch, que represente el estado de un qubit como un vector tridimensional móvil y permita aplicar compuertas cuánticas unitarias para animar las rotaciones vectoriales correspondientes de manera fluida y didáctica.

OBJETIVOS ESPECÍFICOS
- Crear un entorno virtual 3D con ejes de coordenadas etiquetados (|0>, |1>, |+>, |->, |i>, |-i>) representando los polos y el ecuador cuántico.
- Desarrollar un motor de cálculo matemático tridimensional que traduzca las amplitudes complejas de los estados cuánticos (ángulos theta y phi) a coordenadas cartesianas tridimensionales.
- Diseñar un sistema de animaciones suaves que muestre la trayectoria recorrida por el vector de estado sobre la superficie esférica al aplicar transformaciones matriciales.
- Implementar una interfaz táctil y de ratón para rotar y explorar la esfera desde cualquier ángulo, facilitando la comprensión espacial.

JUSTIFICACIÓN
La visualización en tres dimensiones es una de las herramientas más potentes para simplificar teorías matemáticas abstractas. BlochSphereVis se justifica porque permite a los alumnos interactuar directamente con la geometría cuántica. En lugar de ver fórmulas complejas de cosenos y senos hiperbólicos de fase, los estudiantes pueden ver en tiempo real cómo la compuerta Hadamard toma el vector del polo norte (|0>) y lo gira 90 grados alrededor del eje Y para dejarlo en el ecuador (|+>). Esto convierte el aprendizaje en un proceso intuitivo e interactivo.

USUARIOS FINALES
- Usuario Estudiante de Física Cuántica: Experimenta con el vector de estado del qubit aplicando secuencias de compuertas y observando las trayectorias de fase resultantes.
- Usuario Docente / Conferencista: Emplea la interfaz tridimensional interactiva como proyector en conferencias académicas para ilustrar clases de álgebra lineal compleja y mecánica cuántica básica.

LISTA DE FUNCIONALIDADES POR TIPO DE USUARIO
Funcionalidades del Usuario Estudiante de Física Cuántica:
1. Esfera de Bloch 3D Interactiva: Modelo de esfera rotable por arrastre de ratón que muestra el vector de estado actual.
2. Consola de Compuertas Unitarias: Botonera interactiva para aplicar compuertas clásicas (X, Y, Z, H, S, T) y observar la rotación en vivo del vector.
3. Control Deslizante de Ángulos (Theta y Phi): Mandos deslizantes para mover libremente el vector introduciendo ángulos en radianes, actualizando en tiempo real la notación bra-ket del estado en pantalla.
4. Historial de Operaciones: Registro de compuertas aplicadas que permite deshacer o rehacer movimientos espaciales.

Funcionalidades del Usuario Docente / Conferencista:
1. Creador de Animaciones de Exposición: Herramienta para guardar trayectorias predefinidas (ej. demostración del entrelazamiento conceptual o desfasamiento) y reproducirlas como un video explicativo paso a paso.
2. Exportador de Estados: Módulo para extraer las coordenadas complejas actuales del qubit en formato JSON para análisis matemático externo.

LISTA DE TECNOLOGÍAS A APLICAR
- Entorno Gráfico Tridimensional: WebGL, Three.js, OrbitControls.
- UI del Panel de Control: React.js, Tailwind CSS, dat.GUI (opcional para controles de física).
- Matemática y Matrices: Math.js para el cálculo exacto de productos de matrices de matrices unitarias de 2x2.

BIBLIOGRAFÍA CONSULTADA
- Russell, S., & Norvig, P. (2020). *Inteligencia artificial: un enfoque moderno*. Pearson.
- Nielsen, M. A., & Chuang, I. L. (2010). *Quantum Computation and Quantum Information*. Cambridge University Press.
- Joyanes Aguilar, L. (2020). *Inteligencia artificial y computación cognitiva*. Alfaomega.
