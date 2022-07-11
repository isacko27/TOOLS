#Autor: Aarón Salas Alvarado(2022437501)
#Coautores: Samuel Gomez Villanueva y Pamela Rojas

# Ejercicio 1
# El numero de entrada debe ser natural
# La salida indica si el numero de entrada es par o impar
def par_impar(num):
    if num <= 0:
        return "ERROR:NUMERO DEBE SER NATURAL"
    if (num % 2) == 0:
        return "NUMERO ES PAR"
    else:
        return "Numero es impar"


# Ejercicio 2
# Tres datos de entrada, 2 datos numericos y un string
# El string no puede ser distinto a +, -, /, *
# Los strings definen una funcion matematica entre los numeros
# Imprimir el resultado de la operacion matematica
def minicalculadora(op, n1, n2):
    if op == "*" or "/" or "-" or "+":
        if op == "*":
            return n1 * n2
        else:
            pass

        if op == "/":
            if n2 != 0:
                return n1 / n2
            else:
                return "ERROR: DIVISOR DEBE SER DIFERENTE A 0"

        if op == "+":
            return n1 + n2

        if op == "-":
            return n1 - n2

    else:
        return "ERROR: CÓDIGO DE OPERACIÓN DEBE SER: +, -, /, *"


# Ejercicio 3
# 3 datos numericos de entrada
# Las cifraz deben ser numeros naturales
# no se permiten usar funciones preconstruidas
# El programa detemina cual de los 3 datos numericos tiene mayor valor
def mayor(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1, "ES EL NUMERO MAS ALTO"
    if n2 > n1 and n2 > n3:
        return n2, "ES EL NUMERO MAS ALTO"
    if n3 > n1 and n3 > n2:
        return n3, "ES EL NUMERO MAS ALTO"


# Ejercicio 4
# El dato de entrada es una cantidad de colones
# El dato de salida es un desglose de billetes segun la cantidad de colones
# El numero de colones debe ser multiplo de 5000
# Los cálculos se empiezan por el billete más alto hasta llegar al menor
# No debe imprimir las denominaciones innecesarias.
def desglose_billetes(n1):
    if (n1 % 5000) == 0:
        cincuentas = n1 // 50000
        veintes = (n1 - (cincuentas * 50000)) // 20000
        dieces = (n1 - (cincuentas * 50000 + veintes * 20000)) // 10000
        cincos = (n1 - (cincuentas * 50000 + veintes * 20000 + dieces * 10000)) // 5000
        if cincuentas > 0:
            print (cincuentas, "billetes de cincuenta")
        if veintes > 0:
            print (veintes, "billetes de veinte")
        if dieces > 0:
            print (dieces, "billetes de diez")
        if cincos > 0:
            print (cincos, "billetes de cinco")
    else:
        return "LA CANTIDAD DE COLONES DEBE SER MULTIPLO DE 5000"


# Ejercicio 5
# 2 datos numericos de entrada
# retorne un número con los dígitos que tienen en común esas entradas
# El resultado no debe tener dígitos repetidos.
# Sino tienen dígitos en común retorne -1
# valide que sean de 3 dígitos
def digitos_en_comun(n1, n2):
    if 1000 > n1 >= 100 or 1000 > n2 >= 100:
        u1 = n1 % 10
        d1 = n1 % 100 // 10
        c1 = n1 // 100
        u2 = n2 % 10
        d2 = n2 % 100 // 10
        c2 = n2 // 100

        if u1 == u2 or u1 == d2 or u1 == c2:
            digitouno = u1
        else:
            digitouno = 0

        if d1 == u2 or d1 == d2 or d1 == c2:
            digitodos = d1
        else:
            digitodos = 0

        if c1 == u2 or c1 == d2 or c1 == c2:
            digitotres = c1
        else:
            digitotres = 0

        return (digitouno * 100) + (digitodos * 10) + digitotres
    else:
        return "ERROR: EL NUMERO DEBE DE SER DE 3 CIFRAS"


# Ejercicio 6
# pasar de una escala numérica a alfabética
# recibir una calificación que es un número natural entre 0 y 100
# Si la cifra no cumple retorna el string “ERROR: NOTA DEBE ESTAR ENTRE 0 Y 100”
#Debe retornar los siguientes valores:
#“A – Excelente (Aprobado)”: notas de 90 a 100
#“B – Bien (Aprobado)”: notas de 80 a 89
#“C – Suficiente (Aprobado)”: notas de 70 a 79
#“D – Deficiente (Reprobado)”: notas de 50 a 69
#“F - Muy deficiente (Reprobado)”: notas de 0 a 49
def calificacion(n1):
    if 0 <= n1 <= 100:
        if 100 >= n1 >= 90:
            return "A – Excelente(Aprobado)"
        if 89 >= n1 >= 80:
            return "B – Bien(Aprobado)"
        if 79 >= n1 >= 70:
            return "C – Suficiente(Aprobado)"
        if 79 >= n1 >= 70:
            return "D – Deficiente(Reprobado)"
        if 49 >= n1 >= 50:
            return "F - Muy deficiente(Reprobado)"
    else:
        return "ERROR: LA NOTA DEBE SER ENTRE 0 Y 100"


# Ejercicio 7
#reciba un número natural de 4 dígitos
# retorne dos valores:
# el primero va a contener la cantidad de todos los dígitos pares
# el segundo la cantidad de todos los dígitos impares
# Validar que el número de entrada esté en el rango indicado
# else retornar el mensaje “ERROR: DEBE SER UN NÚMERO NATURAL DE 4 DÍGITOS”
def contar_pares_impares(n1):
    if n1 >= 1000:
        par = 0
        impar = 0
        u1 = n1 % 10
        d1 = n1 % 100 // 10
        c1 = n1 // 100
        m1 = n1 // 1000
        if u1 % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
        if d1 % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
        if c1 % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
        if m1 % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
        return par, impar
    else:
        return "ERROR: DEBE SER UN NUMERO NATURAL DE 4 DIGITOS"




# Ejercicio 8
# reciba un número natural de 4 dígitos
# retorne dos valores:
# el primero va a contener todos los dígitos pares
# el segundo todos los dígitos impares que aparecen en el número de entrada
# Cuando no hayan dígitos pares o impares imprimir “no hay” en la parte respectiva del resultado
# El orden de los dígitos en los resultados debe ser acorde al orden en el número de entrada
# si el número de entrada no esta en el rango indicado retornar el mensaje “ERROR: DEBE SER UN NÚMERO NATURAL DE 4 DÍGITOS”
def pares_impares(n1):
    if n1 >= 1000:
        par = 0
        impar = 0
        u = n1 % 10
        d1 = n1 % 100 // 10
        c1 = n1 // 100 % 10
        m1 = n1 // 1000

        if m1 % 2 == 0:
            par = par + m1
        else:
            impar = impar  + m1
            pass
        if c1 % 2 == 0:
            par = (par * 10) + c1
        else:
            impar = (impar * 10) + c1
            pass
        if d1 % 2 == 0:
            par = (par * 10) + d1
        else:
            impar = (impar * 10) + d1
            pass
        if u % 2 == 0:
            par = (par*10) + u
        else:
            impar = (impar*10) + u
            pass

        if par == 0:
            return "no hay", impar
        else:
            pass

        if impar == 0:
            return par, "no hay"
        else:
            pass

        if par and impar > 0:
            return par, impar
    else:
        return "ERROR: DEBE SER UN NUMERO NATURAL DE 4 DIGITOS"




# Ejercicio 9
# reciba tres valores numéricos
# Debe retornar los tres valores recibidos en orden descendente
# No se permiten usar funciones preconstruídas
def orden_descendente(n1, n2, n3):
    if n1 > n2 > n3:
        return n1, n2, n3
    if n2 > n3 > n1:
        return n2, n3, n1
    if n3 > n1 > n2:
        return n3, n1, n2
    if n1 > n3 > n2:
        return n1, n3, n2
    if n2 > n1 > n3:
        return n2, n1, n3
    if n3 > n2 > n1:
        return n3, n2, n1




# Ejercicio 10
# Desarrolle la función booleana bisiesto que reciba un año como parámetro
# número natural de 4 dígitos >= 1800
# retorne el valor booleano
# (True) si el año es bisiesto o falso (False) si no lo es
# si no se cumple con la restricción del año retornar el valor False.
def bisiesto(n1):
    if n1 >= 1800 and 10000 > n1 >= 1000:
        if n1 % 4 == 0:
            if n1 % 100 != 0 or n1 % 400 == 0:
                return (True)
            else:
                return (False)
        else:
            return (False)
    else:
        return "El numero debe ser de 4 digitos y mayor a 1800"




# Ejercicio 11
# recibe un entero positivo de 8 dígitos en el formato ddmmaaaa
# determinar si una fecha esta correcta o incorrecta
# el año debe ser >= 1800
# el mes debe estar entre 1 y 12
# el día debe ser según el mes y el año
# Si la fecha esta correcta retorna True de lo contrario retorna False
# reutilice la función bisiesto desarrollada anteriormente
def valida_fecha(fecha):
    dia = fecha // 1000000
    mes = fecha % 1000000 // 10000
    year = fecha % 10000

    if year < 1800:
        return False
    else:
        if mes < 1 and mes > 12:
            return False
        else:
            if dia < 1 and dia > 31:
                return False
            else:
                if bisiesto(year) == True:
                    if mes == 2 and dia > 29:
                        return False
                    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                        if dia > 30:
                            return False
                        else:
                            return True
                    else:
                        return True
                else:
                    if mes == 2 and dia > 28:
                        return False
                    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                        if dia > 30:
                            return False
                        else:
                            return True
                    else:
                        return True


def bisiesto(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False




# Ejercicio 12
# reciba una fecha como un entero de 8 dígitos estructurados así ddmmaaaa
# Debe retornar el nombre del día correspondiente a esa fecha
# algoritmo de Zeller
# validar la fecha reutilice la función valida_fecha
def nombre_dia(fecha):
    if valida_fecha(fecha) == True:  # La funcion validar_fecha(fecha) trabaja con la sub funcion bisiesto(fecha)
        dd = fecha // 1000000  # Descomposicion
        year = fecha % 10000
        mm = (fecha % 1000000) // 10000

        a = int((14 - mm) / 12)  # Zeller
        y = year - a
        m = int(mm + (12 * a) - 2)
        dia = int(dd + y + int(y / 4) - int(y / 100) + int(y / 400) + ((31 * m) / 12)) % 7

        if dia == 0:  # Determinacion del nombre del dia
            return 'domingo'
        elif dia == 1:
            return 'lunes'
        elif dia == 2:
            return 'martes'
        elif dia == 3:
            return 'miercoles'
        elif dia == 4:
            return 'jueves'
        elif dia == 5:
            return 'viernes'
        elif dia == 6:
            return 'sábado'
    else:
        return 'fecha invalida'


def valida_fecha(fecha):
    dia = fecha // 1000000
    mes = fecha % 1000000 // 10000
    year = fecha % 10000

    if year < 1800:
        return False
    else:
        if mes < 1 and mes > 12:
            return False
        else:
            if dia < 1 and dia > 31:
                return False
            else:
                if bisiesto(year) == True:
                    if mes == 2 and dia > 29:
                        return False
                    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                        if dia > 30:
                            return False
                        else:
                            return True
                    else:
                        return True
                else:
                    if mes == 2 and dia > 28:
                        return False
                    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                        if dia > 30:
                            return False
                        else:
                            return True
                    else:
                        return True


def bisiesto(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
