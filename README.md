<h1>ANALIZADOR MACROECONÓMICO</h1>

Este proyecto comprende el cuerpo de una aplicación de escritorio que lleva a cabo la simulación de sistemas económicos, legales e históricos mediante programación modular y orientada a objetos, con una arquitectura que asegura el mejor rendimiento, buenas prácticas de tipado y una interfaz gráfica funcional y agradable para el usuario.

#

<h2><strong>Módulos</strong></h2>
Como ya se mencionó anteriormente, este programa cuenta con una arquitectura modular para brindar espacios reservados para cada ámbito del programa. Estos son los módulos que se implementan:

<h2>Módulos principales</h2>

<h3><strong>1. <code>dinero.py</code> :</strong></h3>

Este módulo maneja la lógica monetaria mediante la posibilidad de crear objetos de una clase `Dinero`, la cual utiliza métodos matemáticos y tipado preciso para calcular depreciación e inflación. Cuenta con métodos para:
- Comprobar el uso de dicho objeto como medio de cambio
- Expresar una lista de precios en relación a dicha unidad monetaria
- Calcular su valor adquisitivo restante tras la inflación en un periodo especificado
- `@staticmethod`: Obtener una lista de inflaciones (en decimales) mensuales entre el periodo establecido
- `@staticmethod`: Calcular la inflación promedio entre el periodo establecido
- `@staticmethod`: Calcular la inflación acumulada según una lista de inflaciones

#

<h3><strong>2. <code>juridico.py</code> :</strong></h3>

Este es el módulo más pequeño, pues solo existen dos elementos dentro de este:
- `function` -> **`get_marco_legal()`**: retorna un diccionario con las tres principales leyes y artículos constitucionales que regulan la moneda en México: Art. 28 Constitucional, Ley Monetaria de los Estados Unidos Mexicanos, Ley del Banco de México.

- `decorator` -> **`validar_denominaciones`**: define las denominaciones actualmente legales para la moneda mexicana y valida que el monto ingresado sea válido; En caso de no serlo, lanza un `ValueError`.

#

<h3><strong>3. <code>modos_produccion.py</code> :</strong></h3>

Este módulo moldea la evolución histórica de la moneda y su transición entre los distintos métodos de producción evaluada con reglas lógicas básicas. Contamos con dos elementos primordiales:
- `class` -> **`ModoProduccion`**: clase hecha para guardar un resumen de cualquier modo de producción que haya existido, pudiendo guardar su nombre, propiedad de los medios, relaciones sociales, tecnologías dominantes y cómo se usaba el dinero en dicho modo. Además cuenta con un método muy importante para la explicación del siguiente elemento de este módulo:
    - *`transicion(bool, bool, bool)`*: Simula la transición de un modo de producción al siguiente en base a 3 condiciones que se deben cumplir.

- `function` -> **`simular_evolucion`**: como su nombre bien dice, simula la evolución de los 5 modos de producción principales que han existido a lo largo de la historia del sr humano: Comunismo, Esclavismo, Feudalismo, Capitalismo y Globalización.

#

<h3><strong>4. <code>comercio.py</code> :</strong></h3>

Este módulo contiene la arquitectura principal del control de la balanza comercial que vamos a ejemplificar dentro del programa. Aquí también contamos con dos elementos principales:

- `class` -> **`Tratado`**: Es un mero apoyo para la correcta simulación de interacciones entre tratados de libre comercio. puede guardar el nombre del tratado, países partícipes, vigencia y aranceles promedio establecidos.

- `class` -> **`BalanzaComercial`**: La cereza de este módulo: comprende toda la lógica para el cálculo y demostración de las interacciones entre países, entre exportación e importación, saldos, socios por tratado, etc. Cuenta con los siguientes métodos:
    - `agregar_transacción(str, str, float | str, str)`: guarda transacciones entre México y otro país, almacenando su fecha, país de destino, monto y tipo de transacción (Exportación o Importación).
    - `saldo_periodo(str, str)`: devuelve el saldo comercial calculado entre el periodo establecido (formato de fechas: "dd/mm/YYYY")
    - `socios_por_tratado(Tratado)`: devuelve la lista de países que hayan tenido alguna transacción con México y que se encuentren en el tratado establecido.
    - `exportaciones()`: devuelve un DataFrame de Pandas que muestra una suma del monto total en exportaciones de los países que tengan alguna transacción con México.
    - `simular(list[str] | Tratado, str, tkinter.Widget)`: Genera un gráfico de barras verticales mostrando el monto (en miles de USD) en exportaciones hacia los países comprendidos en la lista o tratado objetivo por medio de obtención de información de Banxico.

#

<h3><strong>5. <code>main.py</code> :</strong></h3>

El módulo orquestador; la pantalla final; la zona de ejecución: aquí importamos todo lo indispensable de los anteriores 4 módulos, para después construir la aplicación de demostraciones mediante una clase:

- `class` -> **App**: genera la ventana raíz con la librería `tkinter` y, a su vez, agrega un `tkinter.ttk.Notebook` para poder crear una interfaz de pestañas para mayor rendimiento y una mejor comprensión de la aplicación. 
<br>Después, se construyen las 4 pestañas de la aplicación:

    - 1. `tab_dinero()`: pestaña que simula la inflación acumulada y la caída del valor neto por medio de analizar la devaluación de un billete de <span style="font-family: mathjax">$100.00 MXN</span>, mediante la obtención de la inflación acumulada entre los años establecidos.

    - 2. `tab_juridico()`: pestaña meramente ilustrativa que muestra las normas y leyes guardadas en la función `get_marco_legal`

    - 3. `tab_historia()`: pestaña meramente ilustrativa que muestra los resultados de la evolución simulara en el tercer módulo.

    - 4. `tab_comercio()` pestaña que simula la balanza comercial en términos de exportación o importación en un tratado registrado mediante la gráfica generada en el cuarto módulo.
    <br><kbd>Tratados disponibles:<br>| T-MEC | TLCUEM | Alianza del Pacífico | TLC México-Centroamérica |</kbd>

#

<h2>Módulos complementarios</h2>

<h3><strong><code>constants.py</code> :</strong></h3>

En este módulo se guardan constantes predefinidas para la correcta ejecución del primer y cuarto módulo, como las **seriesID** de exportaciones e importaciones de cada país registrado y los tratados disponibles.

<h3><strong><code>utility.py</code> :</strong></h3>

Este módulo lo cree meramente porque no me gustaba la idea de llenar de funciones extra el cuarto módulo. Este módulo comprende dos funciones de utilidad:
1. `get(str, str):` encargada de las llamadas a la API de Banxico para obtener datos.
2. `random_color():` meramente para generar un color aleatorio para las barras de la gráfica del cuarto módulo.

#

<h2><strong> Librerías usadas </strong></h2>

Estas son todas las librerías/módulos externos que se usaron para este proyecto:
<span style="color: gray">NOTA: Los nombres de módulos de color verde son los estándar, los de color blanco son los externos y requieren instalación previa</span>
<pre><code><span style="color: green">typing</span>
requests
<span style="color: green">functools</span>
pandas
matplotlib
<span style="color: green">datetime</span>
<span style="color: green">os</span>
dotenv (<em>python-dotenv</em>)
<span style="color: green">random</span>
</code></pre>