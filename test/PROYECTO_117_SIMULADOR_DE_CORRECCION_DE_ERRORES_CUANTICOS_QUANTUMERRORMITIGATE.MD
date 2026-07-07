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


INFORMACIÓN DE LA PROPUESTA No. 5 (propuesta de prioridad media)
NOMBRE DEL PROYECTO
QuantumErrorMitigate: Simulador y Evaluador de Códigos de Corrección de Errores Cuánticos.
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
Los qubits físicos son extremadamente sensibles al ruido ambiental (decohrencia y pérdida de fase), lo que provoca errores continuos durante los cálculos cuánticos. Para contrarrestar esto, se diseñan códigos de corrección de errores (como el código de tres qubits para bit-flip o el código de Shor de 9 qubits), pero la lógica de codificar un qubit lógico en múltiples qubits físicos, medir síndromes de error sin destruir la superposición y aplicar compuertas correctoras es sumamente difícil de enseñar y comprender de forma abstracta en pizarras teóricas.

OBJETIVO GENERAL
Desarrollar una aplicación web interactiva que funcione como simulador de códigos de corrección de errores cuánticos (QECC). El sistema permitirá simular canales de ruido cuántico (despolarización, bit-flip, phase-flip), aplicar códigos de corrección específicos sobre qubits de prueba, visualizar la medición de los operadores de síndrome y comprobar cómo se recupera el estado cuántico original de forma automática.

OBJETIVOS ESPECÍFICOS
- Desarrollar un simulador de ruido cuántico probabilístico que emule perturbaciones físicas sobre los qubits.
- Programar la lógica matemática de codificación, detección de síndromes y corrección para el código de inversión de bit (3 qubits), el código de inversión de fase (3 qubits) y el código Shor (9 qubits).
- Diseñar una interfaz interactiva donde el estudiante pueda inyectar manualmente un error (ej. compuerta X o Z involuntaria) en un qubit físico y observar cómo el módulo de corrección detecta y corrige la perturbación sin leer el estado lógico interno.
- Implementar métricas estadísticas de fidelidad cuántica (quantum fidelity) para comparar la calidad del estado final con y sin corrección de errores.

JUSTIFICACIÓN
El hardware cuántico real requiere obligatoriamente capas lógicas de corrección de errores para ser funcional. Por ende, la formación en desarrollo de software cuántico demanda entender estos mecanismos preventivos. QuantumErrorMitigate se justifica al proveer un banco de pruebas virtuales e interactivo. Al interactuar con el flujo de inyección y corrección de fallos, los estudiantes comprenden empíricamente un pilar clave: cómo es posible medir operadores de proyección (síndromes de error) para saber dónde ocurrió una falla sin realizar mediciones directas sobre los datos lógicos, protegiendo así la coherencia del sistema.

USUARIOS FINALES
- Usuario Estudiante de Programación Cuántica: Experimenta con canales de ruido, inyecta fallos controlados y evalúa la efectividad de diferentes códigos de corrección en base a la fidelidad del qubit resultante.
- Usuario Docente en Ciencias Físicas: Utiliza el simulador para realizar clases sobre decoherencia cuántica y demostrar cómo se diseñan algoritmos tolerantes a fallos (Fault-Tolerant Quantum Computing).

LISTA DE FUNCIONALIDADES POR TIPO DE USUARIO
Funcionalidades del Usuario Estudiante de Programación Cuántica:
1. Panel de Inyección de Errores: Interfaz gráfica para aplicar de forma interactiva errores de compuertas (Bit Flip X, Phase Flip Z o despolarización) sobre canales específicos.
2. Selector de Código Corrector: Menú para activar la protección de 3-qubits o el código completo de Shor de 9-qubits.
3. Visor de Operadores de Síndrome: Tabla dinámica que muestra los valores propios resultantes de las mediciones de estabilizadores (ej. mediciones Z1Z2 y Z2Z3).
4. Indicador de Fidelidad: Gráfico de aguja que estima el porcentaje de fidelidad del estado del qubit recuperado respecto al original (0% a 100%).

Funcionalidades del Usuario Docente en Ciencias Físicas:
1. Panel de Configuración de Ruido Continuo: Control deslizante para establecer tasas de error probabilísticas por canal y evaluar el límite de tolerancia de fallos del código (umbral cuántico).
2. Generador de Informes de Rendimiento: Módulo para descargar gráficas que comparan la pérdida de fidelidad en función de la profundidad del circuito con y sin la aplicación de códigos correctores.

LISTA DE TECNOLOGÍAS A APLICAR
- Plataforma e Interfaz: React.js, Context API (gestión de estados cuánticos), Tailwind CSS.
- Cálculos Cuánticos y Operaciones: Computo matricial complejo de 8x8 y 512x512 en JavaScript utilizando librerías matemáticas de precisión.
- Gráficos Estadísticos: Chart.js y Canvas2D.

BIBLIOGRAFÍA CONSULTADA
- Russell, S., & Norvig, P. (2020). *Inteligencia artificial: un enfoque moderno*. Pearson.
- Nielsen, M. A., & Chuang, I. L. (2010). *Quantum Computation and Quantum Information*. Cambridge University Press.
- Joyanes Aguilar, L. (2019). *Big Data: Análisis de datos y ciencia de datos en la sociedad de la información*. Dialnet.
