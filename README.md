# Librería de Vectores y Matrices Complejas
Esta librería es un compendio de varias operaciones que se puede hacer con vectores complejos y matrices complejas, 
esa librería contiene las siguientes operaciones:
- Adición de vectores complejos.
- Inverso (aditivo) de un vector complejo.
- Multiplicación de un escalar por un vector complejo.
- Adición de matrices complejas.
- Inversa (aditiva) de una matriz compleja.
- Multiplicación de un escalar por una matriz compleja.
- Transpuesta de una matriz/vector
- Conjugada de una matriz/vector
- Adjunta (daga) de una matriz/vector
- Producto de dos matrices (de tamaños compatibles)
- Función para calcular la "acción" de una matriz sobre un vector.
- Producto interno de dos vectores
- Norma de un vector
- Distancia entre dos vectores
- Revisar si una matriz es unitaria
- Revisar si una matriz es Hermitiana
- Producto tensor de dos matrices/vectores
## Comenzando 
En la carpeta del proyecto debes tener dos archivos llamados:
* VectorComplexLibrary.py
* VectorComplexTest.py
Es importante que estos archivos se encuentren, ya que uno es la librería con todas las operaciones, y el otro contiene el test que más adelante ejecutaremos
para verificar que la librería funciona adecuadamente.
### Pre-requisitos
Debes tener instalado python y algún entorno de desarrollo interactivo(IDE). El IDE que recomiendo, con el cual fue hecho esta librería, es PyCharm.
### Instalación
1. Para instalar python solo debes ir al sitio web oficial de python.
2. Debes ir a la sección de "Downloads" y descargas la última versión que te recomienda. 
3. Una vez que lo tengas descargado, ejecutas el archivo y le das a instalar.
4. Para Pycharm debes hacer lo mismo, ir al sitio web y buscar la opción "descargar".
5. Ejecutas el archivo y aceptas términos y condiciones y le das en instalar.
6. Al tener descargado python, ejecutas Pycharm y abres la carpeta de la librería de complejos.
7. Verás que en un panel de la derecha de Pycharm tendrás todos los archivos de la carpeta que se usaran.
8. Si abres el archivo VectorComplexLibrary.py podrás ver todas las operaciones que contiene la librería.
### Ejecutar el test
Para poder ejecutar el test debes ir al archivo denominado VectorComplexTest.py y abrirlo con ayuda de Pycharm, se ejecuta el código presionando "ctrl + shift + f10".
### Análisis del Test
Con ayuda de la librería numpy y la de randint, el test consta del siguiente mecanismo:
1. Se hace 10 Test por función de la librería, si quisiera aumentar la cantidad de Tests por función, en la variable TESTS del principio puede cambiar al valor que desee.
2. SEED es una variable que con ayuda de randint toma valores aleatorios de 0 hasta 100, esta variable se usa para armar números complejos aleatorios.
3. SEED_2 esta variable es la que nos dara los tamaños de los vectores y de las matrices, al igual que con la anterior se usa randint para que los valores sean aleatorios.
4. Al ejecutar el test debe aparecer que se ejecutaron 17 test, es decir las todas las funciones de la librería.
5. Si por alguna razón votara Error, esto se debe al mal funcionamiento del código, si por el contrario saliera Failure, significa que algún caso de prueba no dio el resultado esperado,
y si da OK, eso es porque el test ejecuto y los casos de prueba pasaron sin ningún inconveniente.
6. Cada vez que se ejecuta el test, los casos de prueba cambian aleatoriamente gracias a que randint, aleatoriza los tamaños y números complejos de las matrices y vectores.
7. Numpy nos ayudará a comparar si nuestros resultados de la librería están acordes a lo esperado.
### Observaciones
Para el correcto funcionamiento de las funciones, se recomienda que los vectores sean escritos en fila y no en columna, es decir
v_f = [1,2,3,4]         ---> este es el vector fila
v_c = [[1],[2],[3],[4]] ---> este es el vector columna
Se tiene que tener en cuenta esto, para que no crear inconvenientes con las funciones, además los resultados de vectores, se darán en fila.
### Construido con
* Python - Lenguaje de Programación
* Pycharm - IDE
* Git - Control de versiones
* GitHub - Aloja las versiones de Git
### Autores
* Wilmer Rodríguez
### Expresiones de Gratitud
Gracias a todo aquel que use esta librería, espero que les sea de ayuda.
