
##? Clase 002 - Variables, métodos
#TODO Glosario: 

#* Variables: Son un espacio asignado en memoria para almacenar un valor.

#* Programación: Es el proceso de darle una serie de instrucciónes al ordenador para cumplir un fin especifico, cuyo caso es el de automatizar tareas y crear una solución a un problema.

#* Tipos de datos: Son categorias en las que podemos clasificar los distintos tipos de valores que se le pueden asignar a una variable. Existen 2 (dos) tipos de datos; simples y compuestos. 

#* Inferencia de tipos: Es el proceso por el cual el intérprete o compilador de un lenguaje infiere/deduce qué tipo de dato corresponde clasificar en base al valor asignado a una variable. Es un proceso automático.

#? ANTES DE EMPEZAR: Es importante tener en cuanta qué es, y en qué se diferencian un intérprete de un compilador.

#* Introducción: En el mundo de la programación, existen dos herramientas fundamentales para ejecutar código: el intérprete y el compilador. Aunque ambos permiten ejecutar programas, lo hacen de maneras diferentes con importantes distinciones.

#* Intérprete: Un intérprete lee y ejecuta el código fuente línea por línea, sin necesidad de traducirlo a otro lenguaje. Es como un traductor simultáneo que interpreta el código fuente para la máquina en tiempo real.

#TODO Ventajas:
'''
    #* 1) Ejecución rápida: El código se ejecuta directamente, sin necesidad de una fase de compilación previa.
    #* 2) Desarrollo interactivo: Permite realizar pruebas y modificaciones al código de forma rápida y sencilla.
    #* 3) Portabilidad: Los programas interpretados son independientes de la plataforma, ya que el intérprete se encarga de traducir el código para la máquina específica.
'''


#TODO: Desventajas:

    #! 1) Menor eficiencia: La interpretación puede ser más lenta que la ejecución de código compilado, ya que el proceso de lectura tendrá que ejecutarse siempre, independientemente de si hay cambios en el codigo o no.
    #! 2) Dependencia del intérprete: El programa necesita el intérprete para poder ejecutarse en cualquier máquina. Por ejemplo, descargar el intérprete de Python para, por ejemplo, Windows. 

#* Compilador: Un compilador traduce el código fuente a un lenguaje que la máquina pueda entender directamente, generalmente el lenguaje máquina. Este proceso de traducción se realiza antes de la ejecución del programa.

#TODO: Ventajas:

    #* 1) Mayor eficiencia: Los programas compilados se ejecutan mucho más rápido que los interpretados, ya que una vez compilados, no necesita volver a traducir el programa a código máquina.
    #* 2) Independencia del intérprete: El programa compilado no necesita un intérprete para ejecutarse en cualquier máquina.

#TODO: Desventajas:

    #! 1) Proceso más complejo: La compilación requiere un paso adicional antes de la ejecución del programa.
    #! 2) Menor portabilidad: El código compilado está ligado a la plataforma para la que se compiló, haciendo énfasis en el desarrollo para una plataforma en especifico, por ejemplo, Linux.

#TODO: Habiendo quedado claro estos conceptos, podemos empezar!

##? Variables

#* Ya sabemos que las variables son un espacio asignado en la memoria del dispositivo que sirven para almacenar un valor, anteriormente hemos estado trabajando con variables, asignandoles un valor y distintos tipos de datos. También habiamos visto las buenas prácticas que se deben llevar a cabo para nombrar una variable, siendo estas descriptivas y precisas para un completo entendimiento. Pero, ¿Qué comportamientos tienen las variables?

#* 1) Asignación: Como ya hemos visto, para crear una variable en Python, se utiliza el nombre de la variable seguido del operador de asignación (=) y el valor que se le quiere asignar.

#Ejemplo: 

nombre = "Juan Perez" #String
edad = 21 #Integer
casado = True #Boolean

#* 2) Tipos de datos: Las variables pueden almacenar diferentes tipos de datos, como números, cadenas de texto (strings), caracteres (@, !, -, etc), booleanos (True o False). Python es un lenguaje débilmente tipado, por lo que no es necesario especificar el tipo de dato al declarar la variable, ya que el intérprete lo deduce automáticamente.

#* 3) Alcance o scope: El alcance de una variable se refiere a la parte del código donde es visible y accesible. Las variables pueden tener un alcance global (visibles en todo el programa) o local (visibles solo dentro de una función o bloque de código).

#Ejemplo: 

# Variable global
variable_global = 10 #Va a poder ser accedida desde todo el programa.

def mi_funcion():
    # Variable local
    variable_local = 5 #Esta la vas a poder acceder desde el propio metodo donde está declarada, no fuera.
    print("Variable local dentro de la función:", variable_local)

#* Accediendo a la variable global desde dentro de la función
def otra_funcion():
    print("Variable global dentro de otra función:", variable_global)

#! Intentando acceder a la variable local fuera de su ámbito
def funcion_fuera():
    print("Intentando acceder a la variable local fuera de su ámbito:", variable_local)

#* Llamando a las funciones o invocandolas. 
mi_funcion()
otra_funcion()
#*TRY: EXCEPT: SIRVE PARA MANEJAR LOS ERRORES O EXCEPCIONES
try:
    #* Fuera de las funciones, intentamos acceder a la variable local
    #! Esto dará un error ya que la variable local solo es válida dentro de la función mi_funcion
    funcion_fuera()
except NameError:
    print("Error de scope, pero el programa seguirá su ejecución");


#* 4) Modificación:

#* El valor de una variable puede ser modificado después de su declaración.

#Ejemplo:

edad = 21 #? Asignamos a nuestra varaible "edad" el valor 21
edad = 22 #? A nuestra misma variable "edad" le RE-ASIGNAMOS un valor

print(edad);
#* 5) Operadores:

#* Las variables se pueden utilizar en expresiones con operadores aritméticos, lógicos y de comparación.

#Ejemplo:

resultado = edad + 10
print(resultado) #? Salida: 32

#Asignando operadores de comparacion que devuelven true o false;
resultado = 10 != 24;
print(resultado);

#* 6) Funciones:

#* Las variables se pueden pasar como argumentos a funciones y también se pueden usar dentro de las funciones.

#Ejemplo:

def saludar(nombre):
  print(f"Hola {nombre}")

saludar("Juan")

#* 7) Borrado:

#* Las variables pueden ser eliminadas del programa utilizando la función del.

#Ejemplo:

nombre = "Juan Perez"
del nombre

try: 
    print(nombre) #? Salida: NameError: name 'nombre' is not defined
except NameError: 
    print("NameError: La variable 'nombre' no está definida. Continuando ejecucion del código.")

nombre = input("Ingrese su nombre: "); #TODO: INPUT ES PARA INGRESAR DATOS POR CONSOLA. 
email  = input("Ingrese su email: "); #TODO: INPUT ES PARA INGRESAR DATOS POR CONSOLA. 
contrasena = input("Ingrese su contraneña: "); #TODO: INPUT ES PARA INGRESAR DATOS POR CONSOLA. 
dni  = input("Ingrese su DNI: "); #TODO: INPUT ES PARA INGRESAR DATOS POR CONSOLA. 


def registro(nombre, email, contrasena, dni): 
    if nombre != None and email != None and contrasena != None and dni != None :
        nombre = nombre;
        email = email;
        contrasena = contrasena;
        dni = dni;
        DATOS_PERSONALES = f"Bienvenido: {nombre} a nuestra app! Sus datos: 1)Email: {email}. DNI: {dni}";
        print(DATOS_PERSONALES);
    else: 
        print("Una o mas propiedades están faltando");


registro(nombre, email, contrasena, dni);



#* En resumen: Las variables son elementos fundamentales en la programación. Permiten almacenar datos y utilizarlos en diferentes partes del código. El comportamiento de las variables depende de su tipo de dato, alcance, ámbito y las operaciones que se realicen con ellas.

##? PLUS: Buenas prácticas: Además de los conceptos básicos sobre variables, es importante seguir algunas buenas prácticas al trabajar con ellas en Python. Estas prácticas ayudan a mejorar la legibilidad y entendimiento del código:

#*1) Uso de comentarios: Aunque es importante nombrar las variables de manera descriptiva, a veces el propósito de una variable puede no ser obvio solo con su nombre. En estos casos, es útil agregar comentarios para explicar qué hace la variable y cómo se usa. Esto es especialmente importante en código complejo o en colaboración con otros desarrolladores, ya que facilita la comprensión del código.

#EJEMPLO

# Calcular el promedio de edad
try: 
    promedio_edad = (edad1 + edad2 + edad3) / 3
    print(promedio_edad);
except NameError:
    print("NAME ERROR: Una o mas variables no están definidas");

#* 2) Constantes: Las constantes son variables cuyo valor no cambia durante la ejecución del programa. En Python, las convenciones de estilo sugieren que los nombres de las constantes se escriban en mayúsculas, con palabras separadas por guiones bajos si es necesario para mejorar la legibilidad. Esto ayuda a distinguir las constantes de las variables normales y hace que el código sea más claro.

PI = 3.14159 #Constante de PI
GRAVEDAD = 9.8 #Constante de la gravedad

#* Manejo de errores: Es importante manejar adecuadamente los errores relacionados con las variables en Python. Por ejemplo, si intentas acceder a una variable que no ha sido definida, Python lanzará un error de NameError. Si se produce un error de tipo al intentar realizar una operación con variables de tipos incompatibles, Python lanzará un error de TypeError. Es importante anticipar estos posibles errores y manejarlos adecuadamente en tu código.

try:
    resultado = edad + "10"  # Intentar sumar un número con una cadena
except TypeError:
    print("Error: No se puede sumar un entero con una cadena")

#* Convenciones de estilo: Siguiendo las convenciones de estilo comunes, como PEP 8, se recomienda utilizar el estilo snake_case para nombrar variables en Python. Esto significa que los nombres de las variables deben ser en minúsculas, con palabras separadas por guiones bajos para mejorar la legibilidad. Además, es importante mantener la consistencia en la nomenclatura a lo largo del código para evitar confusiones.

nombre_completo = "Juan Perez"
contador_productos = 10

#TODO: Ahora si, continuemos con lo que nos toca:

#? Métodos o funciones. 

#? ¿Qué es un método?

#* Un método o función es un bloque de código reutilizable que encapsula una serie de instrucciones diseñadas para realizar una acción específica. Los métodos son utilizados para modularizar el código, lo que significa que puedes definir una vez un conjunto de instrucciones y luego invocarlas en cualquier momento y en cualquier lugar dentro de tu programa. Los métodos pueden aceptar argumentos, realizar cálculos, modificar datos y devolver resultados, lo que los hace una herramienta poderosa para organizar y controlar el flujo de tu programa.

#TODO: Veámos como declarar un método!

#! IMPORTANTE: Para la declaración de métodos, es vital ser lo más descriptivo y preciso al momento de nombrarlo, ya que esto asegura una completa legibilidad del código y proporciona buenas prácticas como desarrollador. 

#Para declarar un método, solo basta con usar la palabra reservada "def" (sin comillas), seguido del nombre del método en cuestión, paréntesis y : (dos puntos).

def realizar_suma(): #? Declaración del método "realizar_suma"
    numero1 = 10;
    numero2 = 35;
    resultado = numero1 + numero2;
    #? Cuerpo del método
    return resultado; 
def realizar_pago() :
    nombre_cliente = "Agustin";
    email = "agustol123@gmail.com";
    edad = 24;
    productos = "Jabon, aceite, quitamanchas.";
    precio_total = 5000;
    print(realizar_suma());
    ticket_compra = f"{nombre_cliente} con correo de: {email} y edad de: {edad}, ha adquirido los siguientes productos: {productos} con un precio total de: {precio_total} Pesos argentinos";
    return ticket_compra;

print(realizar_pago);

#* Parámetros o argumentos en los métodos. Como hemos podido observar en el ejemplo anterior, al construir los métodos, hay una parte en donde tiene explicito un paréntesis. Los paréntesis significan que desde dentro es CÓMO se le pasarán datos/información externa a nuestros métodos, ya que estos por si mismos no son capaces de acceder a información externa, pero, ¿Qué es un parámetro?

#* Los parámetros en las funciones son variables que se definen en la declaración de la función y que reciben valores cuando la función es llamada. Estos valores proporcionados al llamar a la función se conocen como argumentos. Los parámetros permiten que una función acepte datos de entrada, los cuales pueden ser utilizados dentro del cuerpo de la función para realizar operaciones, realizar cálculos, o cualquier otra tarea que la función deba realizar.

#TODO: Veamos un ejemplo!

def saludar(nombre): #Creamos nuestro método "saludar"
    print("Hola,", nombre) #Imprimimos en consola (con la función "print") el saludo, más el nombre de la persona almacenado en la variable nombre

saludar("Juan") #Llamamos a nuestro método saludar, pasándole como parámetro el string "Juan" en lugar de una variable.

#TODO: También podriamos hacer esto: 

nombre_persona = "John";

def saludar(nombre):
    print("Hola, " + nombre);

saludar(nombre_persona);

#* En nuestro ultimo caso, hemos creado una variable llamada nombre_persona que almacenará el string "Juan". Luego, hemos definido exactamente el mismo método para saludar, que recibe como parámetro un nombre y lo usa para imprimir en consola el saludo dedicado a esta persona.

#! RECUERDA: En los métodos, dentro de los paréntesis, los nombres también deben ser descriptivos y precisos sobre QUÉ datos se espera recibir en la función. Además de que al momento de CREAR la función, estos nombres actuan si se estuvieran creando variables, no usando las existentes.

#! IMPORTANTE: En Python no existe la sobrecarga de métodos, y fuera de la Programación Orientada a Objetos, no es posible sobreescribir un método, por lo que no podriamos hacer esto: 

def realizar_suma(): #? Declaración del método "realizar_suma"
    numero1 = 10;
    numero2 = 35;
    resultado = numero1 + numero2;
    #? Cuerpo del método
    return resultado; #? Retorno de un valor

def realizar_suma(num1, num2):
    resultado = num1 + num2;
    return resultado;

try: 
    print(realizar_suma()) #? Salida: TypeError
except TypeError:
    print("ERROR: TypeError, no se sabe a qué variable python debe llamar");

#* En este caso, Python no puede determinar a qué función realizar_suma se debe llamar, ya que hay dos funciones con el mismo nombre pero diferentes parámetros. Para evitar este error, se debe usar un nombre diferente para la segunda función.

#TODO: ¿Has notado que los métodos tienen una palabra reservada llamada "return"?

#* En la programación, un método puede devolver un valor, o simplemente realizar una operación sin devolver ningún valor. Por ejemplo, volvamos a nuestro método saludar.

nombre_persona = "John"

def saludar(nombre):
    print("Hola, " + nombre);

saludar(nombre_persona);

#* En este caso, no hay ningun retorno de valores, pero sí que nuestro método está haciendo algo. En este caso, se está imprimiendo en consola el saludo a la persona, pero podriamos hacer lo mismo de la siguiente manera: 

nombre_persona = "John"

def saludar(nombre):
    return "Hola, " + nombre;

print(saludar(nombre_persona)); 
#* En este caso, el resultado es el mismo pero con unos pasos adicionales. Estamos haciendo uso de la palabra reservada "return" para devolver el valor, en este caso el saludo. Luego, dentro de la función print, estamos invocando a nuestro método saludar, que nos devolverá el saludo como valor y print lo imprimirá en consola. 

def realizar_suma(num1 , num2):
  num1 = 20 ;
  num2 = 20 ;
  resultado = num1 + num2 
  print(resultado)  
realizar_suma(40 , 60)