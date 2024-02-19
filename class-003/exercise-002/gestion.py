import uuid;

def generar_uuid(): return str(uuid.uuid4())

class GestionColegio():
    __lista_alumnos = [];
    __lista_cursos = [];
    __lista_profesores = [];

    def cargar_datos(self):
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        edad = input("Ingrese la edad: ")
        dni = input("Ingrese el DNI: ")
        es_alumno = int(input("¿Es un alumno o un profesor? Presione 1 para alumno y 2 para profesor: "));
        if not nombre or not apellido or not edad or not dni or not es_alumno:
            print("Uno o mas campos están faltando");
        else:
            if es_alumno == 1:
                miAlumno = Alumno(nombre, apellido, edad, dni, 0, 0);
                miAlumno.setRole("Alumno")
                print(f"El nombre es: {miAlumno.getNombre()} {miAlumno.getApellido()}. \nEdad: {miAlumno.getEdad()}.  \nDNI: {miAlumno.getDni()}");
                return miAlumno;
            elif es_alumno != 2:
                print("Eleccion no válida");
            else: 
                especialidad = input("Iscriba la especialidad del profesor: ");
                experiencia_laboral = int(input("Ingrese los años de experiencia laboral: "));
                if not especialidad or not experiencia_laboral: 
                    print("Uno o mas campos están faltando");
                else:
                    miProfesor = Profesor(nombre, apellido, edad, dni, especialidad, experiencia_laboral);
                    miProfesor.setRole("Profesor");
                    print(f"El nombre es: {miProfesor.getNombre()} {miProfesor.getApellido()}. \nUUID: {miProfesor.getCodEmpleado()}. \nEdad: {miProfesor.getEdad()}.  \nDNI: {miProfesor.getDni()} \nEspecialidad: {miProfesor.getEspecialidad()}. \nAños de experiencia: {miProfesor.getExperienciaLaboral()}");
                    return miProfesor;
            

    def guardar_datos(self, objeto):
        if objeto.getRole() == "Alumno":
            self.__lista_alumnos.append(objeto);
            for alumno in self.__lista_alumnos:
                print(f"Nombre: {alumno.getNombre()} {alumno.getApellido()}, Edad: {alumno.getEdad()}, DNI: {alumno.getDni()}");
        elif objeto.getRole() == "Profesor":
            self.__lista_profesores.append(objeto)
            for profesor in self.__lista_profesores:
                print(f"Nombre: {profesor.getNombre()} {profesor.getApellido()}, Edad: {profesor.getEdad()}, DNI: {profesor.getDni()}, Especialidad: {profesor.getEspecialidad()}, Años de experiencia: {profesor.getExperienciaLaboral()}");
        else: 
            print("La entidad no corresponde a una persona permitida para guardar en sistema.")
    def crear_curso(self):
        nombre_curso = input("Ingrese el nombre del curso: ");
        duracion = int(input("Ingrese la duracion del curso en numeros para semanas: "));
        id_profesor = input("Ingrese el UUID del profesor para asignar al curso: ");
        minimo_aprobar = input("Ingrese la nota minima para aprobar el curso: ");
        nota_promocionar = input("Ingrese la nota promocionar el curso: ");

        if not nombre_curso or not duracion or not id_profesor or not minimo_aprobar or not nota_promocionar:
            print("Uno o más valores están faltando");
        else: 
            for profesor in self.__lista_profesores:
                if profesor.getCodEmpleado() == id_profesor:
                    curso = Curso(nombre_curso, duracion, profesor.getNombre(), minimo_aprobar, nota_promocionar);
                    print(f"{curso.getCurso()}");
                    return curso;
                else: 
                    print("El ID del profesor no coincide con ninguno registrado.")
class Curso():
    def __init__(self, nombre, duracion, profesor, minima_aprobar, nota_promocionar):
        self.__uuid = generar_uuid();
        self.__nombre = nombre;
        self.__duracion = duracion;
        self.__profesor = profesor;
        self.__minima_aprobar = minima_aprobar;
        self.__nota_promocionar = nota_promocionar;
    def getCurso(self):
        return f"UUID: {self.__uuid}. Curso: {self.__nombre}. Duración: {self.__duracion} semanas. Profesor asignado: {self.__profesor}. Nota mínima para aprobar: {self.__minima_aprobar}. Se promociona con: {self.__nota_promocionar}";

class Persona():
    def __init__(self, nombre, apellido, edad, dni):
        self.__nombre = nombre;
        self.__apellido = apellido;
        self.__edad = edad;
        self.__dni = dni;
    #GETTER
    def getNombre(self):
        return self.__nombre;
    def getApellido(self):
        return self.__apellido;
    def getEdad(self):
        return self.__edad;
    def getDni(self):
        return self.__dni;
    def getRole(self):
        return self.__role;
    #SETTER
    def setNombre(self, nombre):
        self.__nombre = nombre;
        return self.__nombre;
    def setApellido(self, apellido):
        self.__apellido = apellido;
        return self.__apellido;
    def setEdad(self, edad):
        self.__edad = edad;
        return self.__edad;
    def setDni(self, dni):
        self.__dni = dni;
        return self.__dni;
    def setRole(self, role):
        self.__role = role;

class Alumno(Persona):
    __cursos_asignados = [];
    def __init__(self, nombre, apellido, edad, dni, asistencias, ausencias):
        super().__init__(nombre, apellido, edad, dni);
        self.__matricula = generar_uuid();
        self.__asistencias = asistencias;
        self.__ausencias = ausencias;
    def getAsistencias(self):
        print(f"El alumno {self.__Persona__nombre} tiene: {self.__asistencias} asistencias en total");
    def getAusencias(self):
        print(f"El alumno: {self.__Persona__nombre} tiene: {self.__ausencias} inasistencias");
    def getCursosAsignados(self):
        print(self.__cursos_asignados);
    def getMatricula(self):
        print(self.__matricula);

    def setAsistencias(self, asistencias):
        self.__asistencias = asistencias;
        return self.__asistencias;
    def setInasistencias(self, inasistencias):
        self.__inasistencias = inasistencias;
        return self.__inasistencias;
    def setCursosAsignados(self, curso):
        self.__cursos_asignados.append(curso)
        return self.__cursos_asignados;

class Profesor(Persona):
    def __init__(self,  nombre, apellido, edad, dni, especialidad, experiencia_laboral):
        super().__init__(nombre, apellido, edad, dni);
        self.__cod_empleado = generar_uuid();
        self.__especialidad = especialidad;
        self.__experiencia_laboral = experiencia_laboral;
    def getCodEmpleado(self):
        return self.__cod_empleado;
    def getEspecialidad(self):
        return self.__especialidad;
    def getExperienciaLaboral(self):
        return self.__experiencia_laboral;

    def setEspecialidad(self, especialidad):
        self.__especialidad = especialidad;
        return self.__especialidad;
    def setExperienciaLaboral(self, experiencia_laboral):
        self.__experiencia_laboral = experiencia_laboral;

def main():
    try:
        gestionador = GestionColegio();
        while True:
            miEntidad = gestionador.cargar_datos();
            gestionador.guardar_datos(miEntidad);
            eleccion = int(input("Desea seguir creando y guardando alumnos/profesores? 1 para si, 2 para no: "));
            if miEntidad == 2: 
                print("Gracias por usar nuestro sistema");
                break;
            elif eleccion != 1: 
                print("Elección no válida")
                break;
            else: 
                print("Continuando generando más alumnos/profesores")
        while True:
            gestionador.crear_curso();
            eleccion = int(input("Desea seguir creando más cursos? 1 para si y 2 para no."));
            if eleccion == 2:
                print("Gracias por usar nuestro sistema");
                break;
            elif eleccion != 1:
                print("Elección no válida");
                break;
    except Exception as e:
        print(f"Ha habido un error: {e}");

if __name__ == "__main__":
    main();