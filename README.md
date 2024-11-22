
# Análisis de Gramáticas: Cálculo de Conjuntos FIRST y FOLLOW

Este proyecto está diseñado para analizar gramáticas formales y calcular los conjuntos FIRST y FOLLOW para cada símbolo no terminal. Es una herramienta educativa útil para estudiantes y profesionales que trabajan en compiladores, análisis sintáctico y teoría de lenguajes formales.

## Tabla de Contenidos

1. Descripción
2. Características
3. Requisitos
4. Instalación
5. Uso
6. Estructura del Proyecto
7. Ejemplo
8. Contribuciones
9. Licencia

## Descripción

El programa está implementado en Python y permite al usuario ingresar una gramática definida en un archivo de texto. A partir de esta gramática, el programa calcula y muestra los conjuntos FIRST y FOLLOW para cada símbolo no terminal. Estos conjuntos son fundamentales en la construcción de analizadores sintácticos, especialmente en los métodos de análisis predictivo.

## Características

- **Parseo de Gramáticas**: Lee gramáticas desde archivos de texto en un formato específico.
- **Cálculo de Conjuntos FIRST**: Determina los posibles símbolos terminales que pueden aparecer al inicio de las cadenas derivadas de cada no terminal.
- **Cálculo de Conjuntos FOLLOW**: Determina los símbolos que pueden seguir a cada no terminal en las derivaciones.
- **Interfaz de Línea de Comandos**: Interfaz simple para interactuar con el programa mediante la terminal.
- **Soporte para ε-Producciones**: Maneja correctamente producciones que derivan en la cadena vacía (ε).

## Requisitos

- Python 3.6 o superior.

## Instalación

1. **Clonar el Repositorio**:
   ```bash
   git clone https://github.com/josefdc/FirstAndFollows.git
   ```

2. **Navegar al Directorio del Proyecto**:
   ```bash
   cd FirstAndFollows
   ```

3. **Crear y Activar un Entorno Virtual** (Opcional pero Recomendado):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Instalar Dependencias**:

   Este proyecto utiliza únicamente la biblioteca estándar de Python, por lo que no es necesario instalar dependencias adicionales.

## Uso

1. **Preparar el Archivo de Gramática**:

   Crea un archivo de texto (por ejemplo, `grammar1.txt`) con la definición de tu gramática. El formato debe ser el siguiente:

   ```
   SímboloInicial
   NoTerminal -> Producción1 | Producción2 | ... | ProducciónN
   ...
   ```

   Ejemplo:
   ```
   exp
   exp  -> term exp'
   exp' -> + term exp' | - term exp' | ε
   term  -> factor term'
   term' -> * factor term' | / factor term' | ε
   factor  -> ( exp ) | num | id
   ```

   En este ejemplo, `exp` es el símbolo inicial, y las producciones se definen utilizando `->` para separar el lado izquierdo del derecho y `|` para múltiples alternativas. La cadena vacía se representa como `ε`.

2. **Ejecutar el Programa**:

   Desde la terminal, ejecuta el script principal:
   ```bash
   python main.py
   ```

3. **Ingresar el Nombre del Archivo de Gramática**:

   Cuando se te solicite, ingresa el nombre del archivo que contiene la gramática (por ejemplo, `grammar1.txt`).

   ```
   Introduce el nombre del archivo que contiene la gramática: grammar1.txt
   ```

4. **Ver los Resultados**:

   El programa mostrará los conjuntos FIRST y FOLLOW calculados para cada símbolo no terminal.

   **Conjuntos FIRST**:
   ```
   FIRST(exp) = { (, id, num }
   FIRST(exp') = { +, -, ε }
   FIRST(factor) = { (, id, num }
   FIRST(term) = { (, id, num }
   FIRST(term') = { *, /, ε }
   ```

   **Conjuntos FOLLOW**:
   ```
   FOLLOW(exp) = { $, ) }
   FOLLOW(exp') = { $, ) }
   FOLLOW(factor) = { $, ), *, +, -, / }
   FOLLOW(term) = { $, ), +, - }
   FOLLOW(term') = { $, ), +, - }
   ```

## Estructura del Proyecto

```
FirstAndFollows/
├── grammar1.txt       # Archivo de gramática de ejemplo
├── grammar.txt        # Archivo de gramática adicional (puede contener otra gramática)
├── main.py            # Script principal para calcular FIRST y FOLLOW
└── README.md          # Este archivo
```

- **`main.py`**: Contiene la implementación de la clase `Grammar` que maneja el análisis de la gramática y el cálculo de los conjuntos FIRST y FOLLOW. También incluye funciones auxiliares para parsear la gramática desde un archivo y ejecutar el programa.

## Ejemplo

Contenido de `grammar1.txt`:
```
exp
exp  -> term exp'
exp' -> + term exp' | - term exp' | ε
term  -> factor term'
term' -> * factor term' | / factor term' | ε
factor  -> ( exp ) | num | id
```

Ejecución:
```bash
$ python main.py
Introduce el nombre del archivo que contiene la gramática: grammar1.txt
```

**Conjuntos FIRST**:
```
FIRST(exp) = { (, id, num }
FIRST(exp') = { +, -, ε }
FIRST(factor) = { (, id, num }
FIRST(term) = { (, id, num }
FIRST(term') = { *, /, ε }
```

**Conjuntos FOLLOW**:
```
FOLLOW(exp) = { $, ) }
FOLLOW(exp') = { $, ) }
FOLLOW(factor) = { $, ), *, +, -, / }
FOLLOW(term) = { $, ), +, - }
FOLLOW(term') = { $, ), +, - }
```

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, por favor sigue estos pasos:

1. **Fork el Repositorio**.
2. **Crea una Rama de Característica**:
   ```bash
   git checkout -b nueva-caracteristica
   ```
3. **Realiza tus Cambios y Commit**:
   ```bash
   git commit -m "Descripción de la característica"
   ```
4. **Push a la Rama**:
   ```bash
   git push origin nueva-caracteristica
   ```
5. **Abre un Pull Request**.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. 