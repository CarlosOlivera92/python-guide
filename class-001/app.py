##Variable


activa = True;

print(f"Activa: {activa}")

activa = not activa;

print(f"Activa: {activa}")

activa = not activa;

print(f"Activa: {activa}")

CONSTANTE = 18;

print(CONSTANTE);

miVariable = "Lauti"

#Es un espacio reservado en mamoria para almacenar un valor

#Las variables pueden almacenar distintos tipos de datos, como números, cadenas de texto (o también llamados Strings), caracteres (@, !, -, etc), booleanos (true o false). Normalmente es importante especificar el tipo de dato a almacenar en las variables, pero en el caso de python, esto no es necesario. ¿Por qué?
    
#Python es un lenguaje de programación multiplataforma y débilmente tipado. ¿Qué quiere decir? Python puede ser ejecutado en una amplia variedad de entornos, tales como servidores, dispositivos móviles, consolas y ordenadores. Al ser un lenguaje débilmente tipado, no es necesario especificar el tipo de dato que se almacenará en la variable, ya que el intérprete de python deducirá por sí mismo qué tipo de dato corresponde según el valor, este proceso es conocido como "Inferencia de tipos".

#Ventajas: 
    #1)Codigo más sencillo, flexible y conciso.
    #2)Facilidad para principiantes

#Desventajas:
    #1)Erroes dificiles de detectar.
    #2)Menor control de tipo de datos. 

#¡Veamos unos ejemplos!

#En python, declarar una variables es muy sencillo. Solo basta con darle un nombre y seguido especificar un valor. Por convenciones generales, al momento de nombrar variables se debe ser lo más descriptivo y preciso sobre lo que esta misma almacenará, veamos unos ejemplos:

nombre = "Juan Perez"; # Declaramos una variable para almacenar el nombre
edad = 21; # Declaramos una variable para almacenar la edad
estaCasado = True; # Declaramos una variable para almacenar el estado civil
miExpresion = 22 > 24;

#En este ejemplo, hemos creado nuestras primeras tres variables, pero, ¿Qué significa?

#Al crear nuestras variables, le hemos especificado a nuestro ordenador que guarde un lugar en la memoria RAM para almacenar los valores que hemos querido darles. En el primer ejemplo, hemos almacenado un nombre, lo cual corresponde a llamarse String o cadena de texto en el mundo de la programación. En nuestro segundo ejemplo, hemos almacenado la edad de nuestra persona, la cual corresponde a un tipo de dato numérico y en nuestro tercer ejemplo, hemos almacenado un valor booleano. Veamos los nombres de las variables.

#Los nombres de las variables deben ser descriptivos y precisos, siempre ajustándose al valor que se espera recibir. Podríamos también declarar lo siguiente: 


x = "Pepito Sanz"; 
y = 33;
z = False;


#En este ejemplo, hemos utilizado los mismos tipos de datos: String, Numéricos y booleanos, pero le hemos dado nombres genéricos y muy poco descriptivos. Realizar esto es considerado una mala práctica, ya que no solo seremos nosotros quienes lean el código de nuestros programas, sino que también serán otras personas quienes deberán dedicar el triple de tiempo en tratar de deducir nuestro código, y esto se traduce en pérdidas de tiempo sin sentido. Tener buenas prácticas al momento de declarar variables no sólo te hará mejor programador, sino que también te ahorarrás y le ahorrarás muchisimo tiempo y pacienia a futuros desarrolladores. Ahora parece un sin sentido, pero imagina que nuestro programa tuviera 3000 lineas de código...

#Ahora que sabemos lo que es Python y lo que son las variables, pasemos al siguiente tema!

##Tipos de Datos

#En programación, los tipos de datos son las categorías en las que se pueden clasificar los distintos tipos de valores que se le pueden asignar a una variable. En Python, existen diversos tipos de datos básicos y compuestos, nosotros haremos énfasis en los básicos.

#Tipos de Datos básicos: 
    #1)Numéricos:
        #a)Enteros: Números sin decimales, como 1, 2, 3, etc. En programación, son llamados Integer o Int.
        #b)Flotantes o de Punto Flotante: Números con decimales, como 1.5, 2.718, 3.1416, etc. Son comunmente conocidos como Float o Double.
        #c)Complejos: Números que incluyen una parte real y una parte imaginaria, como 1+2j, 3-4x, etc. No hay un nombre común ampliamente utilizado en Python, pero se pueden encontrar referencias como complex number, complex type, complex data type o simplemente complex.
    #2)Cadenas de texto o Strings: Son secuencias de carácteres, como "Hola Mundo", "Juan Perez", "JohnDoe@gmail.com". En programación se pueden identificar como String, pero en otras areas como bases de datos pueden ser llamados CHAR o VARCHAR.
    #3)Booleanos: Valores que pueden ser True (verdadero) o False (Falso).
    #4)None: Un valor especial que especifica la ausencia de un valor. Puede ser identificado como None.

#Veamos ejemplos: 

numeroEntero = 1; #Int o Integer
numeroFlotante = 3.1416; #Float o Double
numeroComplejo = 4 + 3j; #Complex 

numero1 = 1;
numero2 = 2;
resultado = numero1 + numero2;

nombre = "Carlos";
apellido = "Olivera";
correo = "olivera.carlos@gmail.com";
direccion = "agustin magaldi 171";

estaCasado = True;
tieneHijos = False;

#Tipos de datos COMPUESTOS: 

    #1) Objectos
    #2) Listas o tuplas (Arrays)
    #3) Diccionarios: Es una colección de valores en forma de clave : valor. 

miPerro = Animal("Felipe", 4, True); #Objeto
miLista = [1,2,3,4,5,6] #Kista o tupla
miDiccionario = {"nombre": "michael", "apellido": "jordan", "edad" : 42}; #Diccionario

#Inferencia de Tipos:

#Anteriormente había mencionado un concepto particular al cual llamamos Inferencia, pero, ¿Qué es exactamene la inferencia? 

#La Inferencia de Tipos es el proceso por el cuál el intérprete o compilador de un lenguaje deduce el tipo de dato asignado a una variable a partir del valor propiamente asignado. Gracias a esto, el programador no necesita especificar qué tipo de dato le corresponde a esa variable explicitamente, sino que el intérprete lo infiere automáticamente.

#¿Cómo funciona la inferencia en Python?

#En Python, la inferencia de tipos se basa en un algoritmo que analiza el valor asignado a una variable y, en función de ese valor, determina el tipo de dato más adecuado. Por ejemplo, si se asigna a una variable el valor 10, el intérprete inferirá que se trata de un número entero. Si se le asigna el valor "Hola mundo" (entre comillas), el intérprete inferirá que se trata de una cadena de texto.

#Ventajas: 
    #1)Código más sencillo y conciso: No es necesario escribir el tipo de dato de cada variable, lo que hace que el código sea más fácil de leer y escribir.
    #2)Facilidad para principiantes: La inferencia de tipos facilita el aprendizaje de Python, ya que los principiantes no necesitan preocuparse por los tipos de datos.
    #3)Flexibilidad: El código es más flexible, ya que las variables pueden cambiar de tipo de dato a lo largo del programa.
#Desventajas: 
    #1)Errores difíciles de detectar: Si se asigna un valor incorrecto (no deseado) a una variable, el intérprete quizá no detecte el error, lo que puede generar errores difíciles de encontrar, especialmente en programas más grandes y complejos.
    #2)Menor control sobre el tipo de dato: El programador tiene menos control sobre el tipo de dato de las variables, lo que puede ser un problema en algunas situaciones, por ejemplo, si a lo largo de la ejecución del programa se busca pasar de Int a Double.

#Operadores aritméticos

#En la programación como en las matemáticas, es muy común encontrarse y utilizar distintos tipos de operadores aritméticos para nuestros programas. Ya hemos visto uno y el más popular, el operador de asignación (=) al momento de asignarle un valor a nuestras variables. Veamos más en profundidad los operadores que nos encontraremos y utilizaremos a lo largo de estas lecciones, ya que son el corazón de nuestro código. 

#Operador de adición o de suma: + (Suma dos valores.)
#Operador de sustracción o resta: - (Resta un valor de otro.)
#Operador de division: / (Divide un valor por otro.)
#Operador de multiplicación: * (Multiplica dos valores.)
#Operador de módulo: % (Devuelve el resto de la división de un valor por otro)
#Division Entera: // ( Divide un valor por otro y devuelve el cociente entero)

#Ejemplos:

# Suma
resultado = 10 + 5
# Salida: 15

# Resta
resultado = 10 - 5
# Salida: 5

# Multiplicación
resultado = 10 * 5
# Salida : 50

# División
resultado = 10 / 5
# Salida: 2.0

# División entera
resultado = 10 // 5
# Salida: 2

# Módulo
resultado = 10 % 5
# Salida: 0

#Precedencia de operadores:

#Al igual que en las matemáticas, los operadores tienen una precedencia definida que determina en qué orden se evalúan. La precedencia de mayor a menor es: 

    #1) Exponenciación (**)
    #2) Negación unaria (-)
    #3) Multiplicación (*) y División (/, //, %)
    #4) Suma (+) y Resta (-)

#Paréntesis: Se pueden usar paréntesis para forzar un orden de evaluación diferente al de la precedencia natural. Ejemplo: 

#Sin paréntesis: 
# Se evalúa la exponenciación antes que la multiplicación
resultado = 2 ** 3 * 4
# Salida: 32


#Con paréntesis: 
# Se evalúa la suma entre paréntesis antes que la multiplicación
resultado = (2 + 3) * 4
# Salida: 20


#Operadores de comparación

#Los operadores de comparación se utilizan para comparar dos valores y devolver un valor booleano (True o False).

#Operador de igualdad: Este operador se utiliza para comparar distintos valores y se identifica de la siguiente forma; ==
    #Ejemplo: Si quisieramos comparar si dos numeros son iguales, podemos decir: numero1 == numero2, o lo que seria lo mismo: 1 == 1 o 2 == 2. Este operador nos devolverá como resultado un valor booleano independientemente de la operación realizada. Si 1 es igual a 1, este devolverá True (verdadero), ya que efectivamente 1 es igual a 1. En cambio, si decimos que 1 es igual a 2, este nos devolverá False (falso), ya que 1 NO es igual a 2.
    #Esto mismo tambien puede aplicarse a Strings además de números, comparando por ejemplo "carlos" == "carlos", lo cual devolvería como resultado True ya que ambos son idénticos en tipo de dato y valor. En cambio, si dijeramos "carlos" == "sandra", este nos devolvería False, ya que si bien el tipo de dato es el mismo, el valor es distinto y el operador realiza el proceso en base al valor y no al tipo de dato.
#Operador de desigualdad: Un operador que se utiliza para comprobar si dos valores son diferentes, se identifica con !=.
    #Ejemplo: Si quisieramos comprobar que dos valores son distintos el uno al otro, podriamos utilizar el operador != de la siguiente manera: 1 != 2, "carlos" != "raquel", True != False (porque también se pueden comparar valores booleanos), (variable) nombre != Nulo. El resultado de estas comparaciones serán booleanos, en el primer ejemplo la salida sería de True, ya que 1 es distinto o diferente a 2. La segunda salida sería True ya que "carlos" es diferente a "raquel" por más que compartan el tipo de dato. La siguiente salida también sería True, porque True es diferente a False y la ultima salida puede variar dependiendo si la variable tiene o no contenido, por eso se comprueba si es distinto a Nulo. 
#Operador de Mayor Que: Comprueba si un valor es mayor que otro.
    #Ejemplo: Si tuvieramos una variable llamada edad, cuyo valor es de 19 y tuvieramos un programa que calcule si un usuario es mayor o menor de edad, podriamos usar el operador de la siguiente forma: edad > 18. Esta prueba daría como salida True, ya que inicialmente nuestra variable edad tiene como valor 19. Pero si edad cambiase a 17, esta prueba daría como resultado False. Ya que edad ahora seria menor a 18, siendo menor de edad. 
#Operador de Menor Que: Comprueba si un valor es menor que otro.
    #Ejemplo: Al diferencia de nuestro operador Mayor Que, este operador comprobara si el primer valor es MENOR QUE el segundo valor dado. Digamos que tenemos 100 numeros, y nuestro programa debe imprimir esos 100 numeros en la pantalla, para realizar ese proceso se puede utilizar el operador MENOR QUE, para que el programa se detenga al llegar al numero 100 y no imprima números infinitamente. ¿Cómo? Veamos un ejemplo.

# Tenemos una variable que se llamará "numeroImprimir" cuyo valor es 0
numeroImprimir = 0

# Queremos imprimir del 1 al 100
while numeroImprimir < 100:
    # Incrementamos el valor de "numeroImprimir" en 1
    numeroImprimir = numeroImprimir + 1;

    # Imprimimos el valor de "numeroImprimir"
    print(numeroImprimir);

#Este ejemplo utilizando un bucle de tipo While, lo cual ahora no es importante, lo veremos más adelante. 

#Operador Menor o igual que (<=): Comprueba si un valor es menor o igual que otro.
# Menor o igual que:
resultado = 2 <= 1
print(resultado)  # Salida: False

#Operador Mayor o igual que (>=): Comprueba si un valor es mayor o igual que otro.
# Mayor o igual que:
resultado = 2 >= 1
print(resultado)  # Salida: True

#RECURSOS

#Documentación oficial de Python: https://docs.python.org/es/3/

nombre = "Enzo" ;
correo = "enzocaldero@gmail.com" ;
edad = 22 ;
casado = False
tienehijos = None ;
apellido ;

juega_futbol = True ;
constante_pi = 3.14 ;
ciclo_lectivo = 2024 ;

