#Paradigma de programacion: Orientado a Objetos

#Ya hemos visto los conceptos esenciales de la programación y el mismo paradigma imperativo, pero, ¿Qué es la programación orientada a objetos?
#El paradigma orientado a objetos es el paradigma que consiste en trasladar objetos de la vida real a codigo para crear aplicaciones mas escalables y reutilizables. O desde su definicion técnica, la Programación Orientada a Objetos (POO) es un paradigma de programación que se basa en la idea de encapsular datos y comportamiento en objetos. Estos objetos se asemejan a objetos del mundo real, con sus propias características (atributos) y acciones (métodos). 

#¿Qué buscamos en la POO?

    #1) Organizar el código en unidades modulares y reutilizables: Cada objeto representa una entidad única con un propósito específico, lo que facilita la comprensión y el mantenimiento del código.
    #2) Mejorar la escalabilidad: Los objetos pueden ser fácilmente agrupados y reutilizados en diferentes aplicaciones, lo que permite crear soluciones más robustas y escalables.
    #3) Simular el comportamiento del mundo real: Los objetos pueden interactuar entre sí de forma similar a como lo hacen los objetos en el mundo real, lo que facilita la creación de aplicaciones más intuitivas y fáciles de usar.

#Para lograr estos objetivos, la programacion orientada a objetos tiene 4 caracteristicas esenciales:
    #1) Encapsulamiento
    #2) Herencia
    #3) Polimorfismo
    #4) Abstracción

#Encapsulamiento: Los datos y el comportamiento del objeto se agrupan en una sola unidad.
#Abstracción: Se exponen solo las características y funcionalidades esenciales de un objeto, ocultando los detalles de implementación.
#Polimorfismo: Los objetos pueden responder a diferentes mensajes de forma diferente, dependiendo de su tipo.
#Herencia: Los objetos pueden heredar características y comportamiento de otros objetos.

#Ejemplos en la POO: 

#Para crear nuestro primer objeto, ante todo es necesario definir/crear nuestra clase.

class DispositivoMovil(): #Creacion de la clase con la palabra reservada class seguido del nombre de la clase
    ancho: 200 #Atributo
    alto: 400 #Atributo
    peso: 0.75 #Atributo
    bateria: 5000 #Atributo

    def encender(self): #Método: Todos los métodos de clase deben tener la palabra reservada def dentro de sus parentesis.
    #En Python, los métodos de instancia (como encender() en este caso) deben tener self como primer parámetro para referirse a la instancia del objeto en sí mismo.
        print("Encendiendo el dispositivo");
    def apagar(self): #Método
        print("Apagando el dispositivo");


#Aquí hemos creado nuestra primera clase con sus caracteristicas (atributos) y comportamientos (métodos), pero, ¿Qué es una clase?

#Una clase es un molde o recipiente en donde definiremos las caracteristicas y comportamientos de nuestros futuros objetos. En este caso, hemos creado la clase Dispositivo Movil, un molde con el cual podremos crear distintos dispositivos como celulares, tabletas, laptops, relojes. 

#Ahora que hemos creado nuestra clase, es momento de crear nuestros primeros objetos en base a ella.
#Para realizar esto, debemos asignar un nombre al objeto. El proceso es el mismo del de declarar una variable.

#Nombre / asignación / valor
celular = DispositivoMovil(); #Invocación a la clase DispositivoMovil para crear el objeto.
tablet = DispositivoMovil();
laptop = DispositivoMovil();
smart_watch = DispositivoMovil();

#A diferencia de crear una variable, en donde asignariamos el valor es donde invocamos/llamamos a nuestra clase para crear el objeto en base a su molde. A pesar de todo, sigue siendo una variable, pero ahora el tipo de dato que almacena es un tipo de dato compuesto, mas precisamente uno de tipo objeto. Al proceso de creación del objeto se le conoce como instancia o ejemplar. Cuando se habla de instanciar o ejemplificar un objeto/clase, se refiere a la creación de un objeto en sí. 

#¿En que nos beneficia crear un objeto? El punto más fuerte de esto es la reutilización, ya que solamente bastaria crear la clase a utilizar UNA VEZ únicamente y de ella instanciar los distintos objetos que podamos imaginar. Por ejemplo:

#Normalmento si quisieramos crear un dispositivo movil lo haríamos creando un diccionario, como sabemos, otro tipo de dato compuesto cuya organizacion se compone en la relación clave : valor.

#Definimos los métodos para establecer CÓMO se comportará nuestro dispositivo
def encender():
    print("Encendiendo el dispositivo");
def apagar(): 
    print("Apagando el dispositivo");

#Creamos nuestro diccionario con las caracteristicas y comportamientos de nuestro dispositivo.
miCelular = {
    "ancho" : 200,
    "alto" : 400,
    "peso" : 0.75,
    "bateria" : 5000,
    "encender" : encender,
    "apagar" : apagar
} 
miTablet = {
    "ancho" : 200,
    "alto" : 400,
    "peso" : 0.75,
    "bateria" : 5000,
    "encender" : encender,
    "apagar" : apagar
} 
miLaptop = {
    "ancho" : 200,
    "alto" : 400,
    "peso" : 0.75,
    "bateria" : 5000,
    "encender" : encender,
    "apagar" : apagar
} 
miReloj = {
    "ancho" : 200,
    "alto" : 400,
    "peso" : 0.75,
    "bateria" : 5000,
    "encender" : encender,
    "apagar" : apagar
} 

#De esta forma estariamos creando nuestros dispositivos móviles, pero tener que escribir los mismos atributos y comportamientos para cada uno de ellos siendo distintos entre sí no solamente que lleva más tiempo, sino que tambien se traduce en codigo más complicado de leer y recursos en el sistema desperdiciados.

#A todo esto lo prodriamos simplificar como hicimos anteriormente, trabajemos con otro tipo de clase.

class Persona():
  nombre = " "
  apellido = " "
  edad = " "

  def saludar(self):
    print("Hola!!!!");

miPersona = Persona();
miPersona2 = Persona();
miPersona3 = Persona();
miPersona4 = Persona();

#Mas corto, preciso y sencillo, verdad? La programación orientada a objetos viene a cambiar nuestra forma de programar para poder enfocarnos en crear programas más reutilizables, fáciles de leer y escalables en el tiempo.

#Pero esto no es todo! Ahora que hemos visto como crear una clase y un objeto, veamos qué más podemos hacer! 

#? ¿Has notado que hemos definido atributos y métodos? Todos y cada uno de ellos pueden ser utilizados con facilidad!
#* Para poder utilizarlos, basta solamente utilizar la nomenclatura del punto para poder acceder a ellos. ¿Cómo funciona? Veamos.

#*La nomenclatura del punto sirve para acceder a elementos dentro de un objeto y se utiliza con un . luego del nombre del objeto. Por ejemplo, quisieramos acceder al nombre de nuestras personas, haríamos lo siguiente: 

miPersona.nombre;
miPersona.apellido;
miPersona.edad;
#*De esta forma estaríamos accediendo a los atributos de nuestro objeto "miPersona". para mostrarlos en pantalla, basta solamente utilizar el mismo formato:

print(f"Nombre: {miPersona.nombre}");
print(f"Apellido: {miPersona.apellido}");
print(f"Edad: {miPersona.edad}");

#* Y si quisieramos editar los atributos para nuestro objeto "miPersona"?

miPersona.nombre = "Carlos";
miPersona.apellido = "Olivera";
miPersona.edad = 24;

print(f"Nombre: {miPersona.nombre}");
print(f"Apellido: {miPersona.apellido}");
print(f"Edad: {miPersona.edad}");

#*De esta forma estaríamos modificando los atributos para nuestro objeto "miPersona" unicamente, los objetos miPersona2, miPersona3, miPersona4 segurian teniendo los atributos por defecto/predeterminados que definimos en nuestra clase.

#También podemos hacer lo mismo para los metodos:

miPersona.saludar();
miPersona2.saludar();
miPersona3.saludar();
miPersona4.saludar();


#!IMPORTANTE: Si bien esto en python está permitido, se recomienda encarecidamente no hacerlo. Como hablamos de las caracteristicas de la POO, una de ellas es el encapsulamiento. Al acceder directamente a los atributos por medio de la nomenclatura del punto, estamos violando el acuerdo de encapsulamiento y por ende, incumpliendo el paradigma orientado a objetos. 

#*Para trabajar con atributos apropiadamente, debemos hacer que de alguna forma, estos sean exclusivamente privados de la clase. Es decir, que solamente puedan ser manipulados desde la clase a la que pertenecen. 

#*En otros lenguajes de programación se pueden definir la privacidad de los atributos por medio de palabras reservadas para declararlos, y el lenguaje inferirá automaticamente que cierto atributo no debe y no podrá ser accesible desde fuera de la clase. En Python esto no ocurre, pero tennemos una forma de decir quienes lean nuestro código que un atributo es privado de la clase.

#Primero, creamos nuestra clase Cliente:
class Cliente():
    #Definiremos nuestro constructor de clase, ya veremos qué es en profundidad
    def __init__(self, nombre, apellido, email):
        self.__nombre = nombre; # Utilizamos __ (doble guión bajo) para nombrar a nuestros atributos, el guion bajo significa que el atributo está encapsulado y no debe accederse desde fuera de la clase
        self.__apellido = apellido;
        self.__email = email;
    #Luego declaramos métodos de acceso, GET Y SET, para poder acceder a nuestros atributos
    def getNombre(self): #En nuestros métodos, utilizamos la palabra reservada "self" para acceder a nuestros atributos de clase
        print(f"{self.__nombre}");
    def getApellido(self):
        print(f"{self.__apellido}");
    def getEmail(self):
        print(f"{self.__email}");
    #Con los métodos GET (del inglés obtener), se accede a leer los atributos de clase que hemos encapsulado.
    def setNombre(self, nombre):
        self.__nombre = nombre;
        print("Nombre cambiado exitosamente");
    def setApellido(self, apellido):
        self.__apellido = apellido;
        print("Apellido cambiado exitosamente");
    def setEmail(self, email):
        self.__email = email;
        print("Email cambiado exitosamente");
    #Con los métodos SET es la forma en CÓMO podremos modificar los valores de nuestros atributos de clase encapsulados

class MiClase():
    def __init__(self, arg1, arg2, arg3):
        self.__arg1 = arg1;
        self.__arg2 = arg2;
        self.__arg3 = arg3;

miInstancia = MiClase("Enzo", 16, "Caldero");

##TODO: Caracteristicas de la POO:

#* Ya habiamos organizado las caracteristicas que componen a la POO, tales son: Herencia, Encapsulamiento, Abstracción y Polimorfismo, habiendo visto también pequeñas definiciones, pero, ¿Qué significan realmente cada una de ellas y cómo funcionan? 

#? Herencia: La herencia es una de las caracteristicas más importantes de la POO, ya que nos permite crear clases derivadas (hijas o subclases) que compartan/hereden caracteristicas y comportamientos de una superclase (clase padre). 
#* En programación, la herencia puede ser de tres formas: simple, multiple y jerárquica. ¿A qué se refiere cada una?
#La herencia simple es la que permite que una clase pueda heredar de una superclase (clase padre), pero solamente se puede heredad de UNA sola clase. Veamos un ejemplo:

#! Name mangling: Es una tecnica que usa Python para cambiar el nombre del atributo que la subclase hereda de la superclase en tiempo de ejecución

class Animal(): #Definimos nuestra clase animal
    def __init__(self, nombre): #Creamos nuestro constructor de clase
        self.__nombre = nombre; #Asignamos los valores que nos lleguen desde el argumento nombre al atributo privado __nombre
    def saludar(self): #Definimos un método para saludar y usamos self para acceder a nuestros atributos privados
        print(f"Hola, mi nombre es {self.__nombre} y soy un animal!")

class Perro(Animal): #Dentro de los paréntesis al crear la clase, allí va el nombre de la clase de la que se busca heredar, en este caso Animal.
    def __init__(self, nombre,  raza):
        super().__init__(nombre) #Utilizamos la palabra reservada "super" para acceder a los atributos del constructor de la superclase Animal, llamando al constructor de la clase base con el argumento adecuado
        self.__raza = raza;
    def ladrar(self):
        print("¡Guau!");
    def saludar(self):
        print(f"Hola, me llamo {self._Animal__nombre} y mi raza es {self.__raza}.") #Accedemos al atributonombre de la superclase Animal que python nos procesó con Name mangling

#En nuestro ejemplo, hemos creado la clase Animal, que tendrá atributos y métodos genéricos para describir a un animal cualquiera. Luego hemos creado nuestra clase Perro, que heredará los atributos y métodos que reciba de la clase o superclase Animal, compartiendo todas las caracteristicas y comportamientos de Animal a Perro y no al revés.

#Ahora tocará crear nuestros objetos:

#Tendremos un animal genérico
miAnimal = Animal("Lucas");
#Ahora haremos que nuestro animal salude.
miAnimal.saludar();

#Ahora procederemos a crear a nuestro primer perro, o más propiamente dicho, crearemos una instancia de la clase Perro, que hereda atributos y métodos de la clase Animal. 

miPerro = Perro("George", "Golder Retriever");

#Si revisamos los atributos y metodos de nuestro objeto miPerro, vamos a poder observar que tiene también atributos y métodos de la superclase Animal

print(miPerro._Animal__nombre)  # Accede al atributo __nombre de la clase Animal utilizando name mangling
miPerro.saludar();
    
