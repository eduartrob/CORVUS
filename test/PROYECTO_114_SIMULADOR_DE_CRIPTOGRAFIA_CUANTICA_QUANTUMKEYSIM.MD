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


INFORMACIÓN DE LA PROPUESTA No. 2 (propuesta de prioridad media-alta)
NOMBRE DEL PROYECTO
QuantumKeySim: Simulador Interactivo de Protocolos de Distribución de Claves Cuánticas (BB84 y E91).
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
La seguridad informática tradicional se ve amenazada por el avance de las computadoras cuánticas, haciendo necesaria la enseñanza de la criptografía cuántica. Sin embargo, los conceptos de superposición cuántica, bases de polarización fotónica y el teorema de no-clonación resultan difíciles de asimilar sin un simulador interactivo que permita observar cómo los intentos de intercepción por parte de un espía alteran inevitablemente la información, permitiendo a los emisores detectar la intrusión.

OBJETIVO GENERAL
Construir una herramienta interactiva de simulación de distribución de claves cuánticas (QKD) bajo el protocolo BB84, que represente visualmente la transmisión de fotones polarizados entre Alice y Bob, los procesos de medición en diferentes bases físicas y el cálculo de la tasa de error (QBER) ante la presencia de un espía (Eve).

OBJETIVOS ESPECÍFICOS
- Desarrollar un modelo físico digital de polarización fotónica y canales cuánticos que incorpore ruido térmico parametrizable y mediciones destructivas.
- Implementar una interfaz gráfica que detalle paso a paso el protocolo BB84: preparación del estado por Alice, selección de bases, recepción y medición por Bob, y reconciliación pública de bases.
- Diseñar un módulo de interceptación de canal (intrusión de Eve) que permita al usuario actuar como espía y comprobar de qué manera la medición altera el estado del fotón, incrementando el error del canal al 25%.
- Programar un panel estadístico que calcule el porcentaje de error cuántico de bits (QBER) y determine de forma automática si la clave generada es segura o debe ser descartada.

JUSTIFICACIÓN
La educación en ciberseguridad avanzada requiere integrar conceptos cuánticos desde una perspectiva empírica. QuantumKeySim se justifica al ser una herramienta visual que elimina la complejidad de configurar hardware óptico real (láseres, polarizadores, detectores de fotón único), permitiendo recrear todo el experimento criptográfico de forma virtual. De este modo, los estudiantes de seguridad informática pueden asimilar la mecánica de la física cuántica aplicada a la confidencialidad absoluta de la información de manera segura y didáctica.

USUARIOS FINALES
- Usuario Alumno de Ciberseguridad: Realiza experimentos criptográficos virtuales, intercepta canales fotónicos para entender los límites del espionaje e interactúa con el cálculo de claves secretas compartidas.
- Usuario Profesor de Criptografía: Utiliza la simulación como demostración práctica en clase para explicar el principio de indeterminación de Heisenberg y el teorema de no-clonación.

LISTA DE FUNCIONALIDADES POR TIPO DE USUARIO
Funcionalidades del Usuario Alumno de Ciberseguridad:
1. Panel del Canal Cuántico (Alice y Bob): Vista interactiva que muestra el envío secuencial de fotones codificados con sus respectivos ángulos de polarización.
2. Controles de Medición de Bob: Interfaz para seleccionar manualmente las bases de medición (rectilínea o diagonal) y ver los resultados binarios resultantes.
3. Simulador de Intercepción de Eve: Botón para activar un espía en la línea, permitiendo configurar la estrategia de espionaje y observar su impacto.
4. Generador de Claves: Pantalla de reconciliación que muestra las bases descartadas y la clave final compartida.

Funcionalidades del Usuario Profesor de Criptografía:
1. Configuración de Ruido del Canal: Control deslizante para introducir interferencia física aleatoria en el canal cuántico y evaluar la robustez del protocolo.
2. Monitor de Depuración Cuántica: Panel técnico con las matrices de densidad de los fotones en cada tramo del viaje para auditoría matemática.

LISTA DE TECNOLOGÍAS A APLICAR
- Desarrollo del Cliente Web: JavaScript, React, CSS Grid/Flexbox, SweetAlert2.
- Animaciones del Canal Óptico: Anime.js para el flujo dinámico de fotones y filtros ópticos.
- Despliegue y Pruebas: Node.js, Webpack, Babel.

BIBLIOGRAFÍA CONSULTADA
- Russell, S., & Norvig, P. (2020). *Inteligencia artificial: un enfoque moderno*. Pearson.
- Nielsen, M. A., & Chuang, I. L. (2010). *Quantum Computation and Quantum Information*. Cambridge University Press.
- García-Peñalvo, F. J. (2018). *Sistemas de soporte a la decisión en el ámbito académico basado en la minería de datos*. Education in the Knowledge Society (EKS).
