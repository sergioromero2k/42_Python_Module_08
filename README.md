# 42_Python_Module_08
42_Python_Module_08

## The Matrix: Data Engineering Starter

Este proyecto es una inmersión en los fundamentos de la Arquitectura de Datos. El objetivo es dominar el aislamiento de entornos, la gestión de dependencias y la configuración segura de sistemas, utilizando la metáfora de The Matrix para entender la importancia de separar el código de la "simulación" (el entorno global del sistema).

### Resumen del Proyecto

Como Arquitecto de Datos en Zion, debes construir sistemas robustos capaces de resistir ataques (errores de configuración y conflictos de dependencias). El curso se centra en herramientas de supervivencia esenciales: entornos virtuales, gestión de paquetes y variables de entorno.

### Teoría Fundamental a Saber

Para completar este proyecto, debes dominar los siguientes conceptos:

- **Aislamiento de Entornos**: Comprender por qué no se debe usar la instalación global de Python y cómo crear "espacios limpios".
- **Gestión de Dependencias**: Diferencias entre el uso tradicional de pip (`requirements.txt`) y herramientas modernas como Poetry (`pyproject.toml`).
- **Seguridad y Configuración**: Uso de archivos `.env` y variables de entorno para evitar el hardcoding de credenciales sensibles (API keys, DB URLs).
- **Pensamiento Computacional**: Manejo de excepciones (`try-except`) y estructuras de proyectos profesionales.

### Ejercicios y Dificultad

| Ejercicio | Nombre                  | Dificultad       | Conceptos Clave                          |
|-----------|-------------------------|------------------|------------------------------------------|
| Ex00      | Entering the Matrix     | (Fácil)      | `venv`, `sys.prefix`, detección de entornos. |
| Ex01      | Loading Programs        | (Media)    | `pandas`, `pip vs Poetry`, `requirements.txt`. |
| Ex02      | Accessing the Mainframe | (Media)    | `python-dotenv`, variables de entorno, `.gitignore`. |

### Detalles de los Ejercicios

#### Exercise 0: Entering the Matrix (ex0/)

- **Objetivo**: Crear un script que detecte si estás dentro o fuera de un entorno virtual.
- **Requisito**: Mostrar rutas de Python y de instalación de paquetes.
- **Salida Esperada**: Si no hay entorno virtual, debe dar instrucciones de cómo crearlo (`python -m venv`).

#### Exercise 01: Loading Programs (ex1/)

- **Objetivo**: Construir una herramienta de análisis de datos que gestione sus propias librerías.
- **Librerías**: `pandas`, `requests`, `matplotlib`.
- **Entrega**: Debes incluir tanto `requirements.txt` como `pyproject.toml`.
- **Funcionalidad**: El script debe verificar si las dependencias están instaladas antes de ejecutar el análisis.

#### Exercise 02: Accessing the Mainframe (ex2/)

- **Objetivo**: Crear un sistema de configuración segura para una tubería de datos (pipeline).
- **Variables a manejar**: `MATRIX_MODE`, `DATABASE_URL`, `API_KEY`.
- **Seguridad**: Uso estricto de `.gitignore` para no subir jamás el archivo `.env` con secretos reales.

#### Reglas Generales

- **Versión de Python**: 3.10 o superior.
- **Estilo de Código**: Convención `snake_case` y comentarios claros.
- **Prohibición de IA**: No copiar/pegar código de IA sin entenderlo. En la evaluación deberás explicar la lógica de cada función o fallarás el proyecto.
