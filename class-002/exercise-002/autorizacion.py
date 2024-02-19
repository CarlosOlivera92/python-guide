miPersona = None
class Persona:
    def __init__(self, nombre_persona, apellido, edad, dni, email, estadoCivil, contrasena):
        self.nombre = nombre_persona
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
        self.email = email
        self.estadoCivil = estadoCivil
        self.contrasena = contrasena

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre
        return f"El nuevo nombre es: {self.nombre}"

def registro():
    global miPersona
    try:
        nombre_usuario = input("Ingrese su nombre: ")
        apellido_usuario = input("Ingrese su apellido: ")
        email = input("Ingrese su email: ")
        edad = input("Ingrese su edad: ")
        dni = input("Ingrese su DNI: ")
        estado_civil = input("Ingrese su estado civil: ")
        contrasena = input("Ingrese su contraseña: ")
        
        if nombre_usuario and email and edad and contrasena:
            miPersona = Persona(nombre_usuario, apellido_usuario, edad, dni, email, estado_civil, contrasena)
            print(f"Se ha creado un nuevo usuario: {miPersona.nombre}")
        else:
            print("Uno o más propiedades están faltando")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

def iniciar_sesion():
    global miPersona
    if miPersona:
        email = input("Ingrese su email: ")
        contrasena = input("Ingrese su contraseña: ")
        if email == miPersona.email and contrasena == miPersona.contrasena:
            print(f"Se ha iniciado sesión exitosamente. Bienvenido {miPersona.nombre}")
        else:
            print("Credenciales inválidas. No se pudo iniciar sesión")
    else:
        print("No se ha registrado ningún usuario aún.")
def miSuma():
    num1 = 1;
    num2 = 1;
def main():
    try:
        miSuma();
        registro()
        iniciar_sesion()
    except Exception as error:
        print(f"Ha ocurrido un error: {error}")

if __name__ == "__main__":
    main()
