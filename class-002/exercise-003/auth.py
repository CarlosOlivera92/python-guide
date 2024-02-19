#VARIABLES
"""
juan = {"nombre":"juan", "edad": 21};
sofia = {"nombre":"sofia", "edad": 19};
marta = {"nombre":"marta", "edad": 23};
carlos= {"nombre":"carlos", "edad": 40};

misPersonas = [juan, sofia, marta, carlos]

print(misPersonas);

for persona in misPersonas:
    print(persona);
    for elemento in persona:
        print( f"{elemento}: {persona[elemento]}")
"""

usuarios = []; #Creamos un array vacío
#METODOS

"""
misNumeros = [1,2,3,4,5,6,7,8,9,10,11]

for numero in misNumeros:
    if numero == 6:
        continue;
    if numero == 10:
        break;
    print(numero);
"""
#Creamos el método para registrar un usuario
def register(): 
    #Usamos try:except para capturar excepciones (errores) y no permitir que todo el programa caiga
    try:
        while True:
            #Pedimos por consola los campos requeridos para crear el usuario
            name = input("Ingrese su nombre: "); #Input toma lo que el usuario escriba en la consola
            last_name = input("Ingrese su apellido: ");
            age = input("Ingrese su edad: ");
            email = input("Ingrese su correo: ");
            password = input("Ingrese su contraseña: ");

            #Evaluamos si algunos de los campos están faltando
            if not name or not last_name or not age or not email or not password:
                print("Uno o mas propiedades están faltando");
            else: 
                #Si no falta ningun campo, se procederá a crear el usuario
                print("Continuando ejecucion del codigo");
                #CReamos nuestro diccionario para la persona a guardar
                miPersona = {"nombre": name, "apellido": last_name, "edad": age, "email": email, "password": password}                
                #Guardamos nuestra persona en nuestro array de usuarios
                usuarios.append(miPersona);
                #Mostramos el mensaje de que todo ha ido bien
                print("Se ha creado un nuevo usuario");
                miEleccion = int(input("Desea seguir registrando usuarios? Ingrese 1 para si o 2 para no"));
                if miEleccion == 2 :
                    print("Gracias por registrar usuarios");
                    #Devolvemos en consola la lista con la información del usuario creado
                    print(miPersona);
                    print(usuarios);

                    break;
                elif miEleccion != 1: 
                    print("No se pudo procesar su elección")
                    break;

    except ValueError:
        print("Error en el valor de una o más variables.")

#Creamos la función para iniciar sesión
def logIn(): 
    #Tomamos valores desde la consola con input
    while True:
        email = input("Ingrese su correo: "); #Input toma lo que el usuario escriba en la consola
        password = input("Ingrese su contraseña: "); #Input toma lo que el usuario escriba en la consola
        if not email or not password: 
            #Evaluamos si los campos email y contraseña están faltando
            print("No se pudo iniciar sesión porque uno o mas valores están faltando.");
        else: 
            #Si los campos están correctos, seguir con el resto del programa
            print("Continuando ejecución del código");
            #Evaluamos si nuestro correo coincide con algun usuario registrado
            for usuario in usuarios:
                if email == usuario["email"]:
                    if password == usuario["password"]:
                        print("Credenciales correctas, bienvenido!")
                        return; # Salir de la función después de encontrar una coincidencia
                    else:
                        print("Contraseña incorrecta.")
                    # Si encontramos el usuario, salimos del bucle
                    break
                else:
                    print("Ningun usuario coincide con estas credenciales");
#INVOCACIONES

if usuarios:
    logIn() #Llamamos al método log in
else: 
    register() #Llamamos al metodo register
    