#REALIZAR UNA CALCULADORA QUE PUEDA REALIZAR OPERACIONES BÁSICAS COMO SUMA, RESTA, MULTIPLICACION Y DIVISION.

#CREAR LA CLASE CALCULADORA QUE SERÁ EL MOLDE PARA CREAR NUESTRO OBJETO QUE CALCULA ENTRE DOS VALORES.
#REALIZAR LOS MÉTODOS DE CLASE QUE REALICEN LAS OPERACIONES ARITMETICAS MENCIONADAS
#LOS MÉTODOS DE CLASE DEBEN DEVOLVER SU RESULTADO EN CONSOLA.

class Calculadora():
    def __init__(self,num1,num2):
        self.__num1 = num1;
        self.__num2 = num2;
    def sumar(self):
        resultado = self.__num1 + self.__num2
        print(resultado)
    def restar(self):
        resultado = self.__num1- self.__num2
        print(resultado)
    def multiplicar(self):
        resultado = self.__num1 * self.__num2
        print(resultado)
    def dividir(self):
       resultado = self.__num1 // self.__num2
       print(resultado)          

mi_objeto = Calculadora(20,30)
mi_objeto.sumar()
mi_objeto.restar()
mi_objeto.multiplicar()
mi_objeto.dividir()

