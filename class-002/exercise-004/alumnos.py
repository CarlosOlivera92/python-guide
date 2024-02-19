import uuid
import random;

lista_alumnos = [];
cursos = [];
def generar_uuid(): return str(uuid.uuid4())

def cargar_datos():
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    edad = input("Ingrese la edad del alumno: ")
    telefono = input("Ingrese el telefono del alumno: ")
    dni = input("Ingrese el dni del alumno: ")

    if not nombre or not apellido or not edad or not telefono or not dni:
        print("Uno o mas valores están faltando");
    else:
        mi_alumno = {   
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "telefono": telefono,
            "dni": dni
        }
        print(f"El nombre es: {nombre} {apellido}. \nEdad: {edad}. \nTelefono: {telefono}. \nDNI: {dni}");
        return mi_alumno;
    
def definir_cursos():
    nombre_curso = input("Ingrese el nombre del curso: ")
    duracion = int(input("Ingrese la duracion del curso en numeros para semanas: "))
    profesor = input("Ingrese el nombre del profesor: ")
    identifier = generar_uuid(); 
    minimo_aprobar = input("Ingrese la nota minima para aprobar el curso ")
    if not nombre_curso or not duracion or not profesor or not identifier or not minimo_aprobar:
        print("Uno o mas valores están faltando");
    else:
        mi_curso = {   
            "UUID": identifier,
            "nombre": nombre_curso,
            "duracion": f"{duracion} semanas",
            "profesor": profesor,
            "minimo_aprobar": minimo_aprobar,
        }
        return mi_curso;
def guardar_cursos(curso):
    cursos.append(curso);
    print(cursos);

def guardar_alumno(alumno):
    lista_alumnos.append(alumno);
    print("----------------- LISTA ALUMNOS -----------------")
    print(lista_alumnos);

def asignar_curso():
    for alumno in lista_alumnos:
        curso_asignado = random.choice(cursos)
        print(f"Alumno {alumno['nombre']} asignado al curso: {curso_asignado}")
        alumno["curso"] = curso_asignado

def main():
    try:
        while True:
            miAlumno = cargar_datos();
            guardar_alumno(miAlumno);
            eleccion = int(input("Desea seguir cargando mas alumnos? 1 para si, 2 para no: "));
            if eleccion == 2:
                print("Gracias por usar nuestro sistema!")
                break
            elif eleccion != 1:
                print("Eleccion no valida.")
                break;
            else: 
                print("Continue registrando alumnos! ");
        while True:
            curso = definir_cursos();
            guardar_cursos(curso);
            eleccion = int(input("Desea seguir cargando mas cursos? 1 para si, 2 para no: "));
            if eleccion == 2:
                print("Gracias por usar nuestro sistema!")
                break
            elif eleccion != 1:
                print("Eleccion no valida.")
                break;
            else: 
                print("Continue registrando cursos! ");
        asignar_curso();
    except Exception as e:
        return f"Ha habido un error: {e}";
if __name__ == "__main__":
    main()
