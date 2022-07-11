#PRACTICA DE SECUENCIAS PYTHON: FOR, LISTAS, TUPLAS, STRINGS
#Autor: Aarón Salas Alvarado(2022437501)
#Coautores: Samuel Gomez Villanueva y Pamela Rojas

#EJERCICIO 1
#RECIBE UNA TUPLA DE STRINGS Y RETORNA UN STRING CON LOS DIGITOS ENCONTRADOS EN LA TUPLA
#ENTRADA: UNA TUPLA
#SALIDA: LOS DIGITOS DENTRO DE LA TUPLA

#PROGRAMA CON FOR
def obtener_digitos_for (tupla):
    if isinstance (tupla, tuple) == False:              #RESTRICCIONES
        return "ERROR: INGRESE UNA TUPLA"
    digitos = ""
    for string in tupla:                                #ANALIZAR CADA ELEMENTO DE LA TUPLA
        if isinstance (string, str) == False:           #RESTRICCIONES
            return "ERROR: LOS ELEMENTOS DE LA TUPLA DEBEN SER TIPO STRING"
        for numero in string:                           #ANALIZAR CADA ELEMENTO DEL STRING
            if numero in "0123456789":                  #VERIFICAR SI ES UN NÚMERO
                if numero not in digitos:
                    digitos = digitos + numero          #AGREGAR EL NÚMERO AL RESULTADO
    return digitos

#PROGRAMA CON WHILE
def obtener_digitos_while(tupla):
    if isinstance(tupla, tuple) == False:               #RESTRICCIONES
        return "ERROR: LA ENTRADA DEBE SER UNA TUPLA"
    indice = 0
    digitos = ""
    while indice < len(tupla):                          #SE CICLA HASTA LLEGAR A LA CANTIDAD DE ELEMENTOS TOTAL DE LA TUPLA
        if isinstance(tupla[indice], str) == False:     #RESTRICCIONES
            return "ERROR: TODOS LOS ELEMENTOS DE LA TUPLA DEBEN SER DE TIPO STRING"

        indice2 = 0

        while indice2 < len(tupla[indice]):             #SE CICLA HASTA LLEGAR A LA CANTIDAD DE ELEMENTOS TOTAL DE LA TUPLA
            if tupla[indice][indice2] in "0123456789":  #VERIFICAR QUE SEA UN NÚMERO
                if tupla[indice][indice2] not in digitos:
                    digitos = digitos + tupla[indice][indice2] #AGREGAR EL NÚMERO AL RESULTADO
            indice2  = indice2 + 1
        indice = indice + 1
    return digitos



#EJERCICIO 2
#RECIBE UN STRING Y RETORNA EL MISMO SIN ESPACIOS Y CON EL NÚMERO DE ESPACIOS QUE HABIAN PRIMERAMENTE EN ESTE
#ENTRADA: UN STRING
#SALIDA: UN STRING SIN ESPACIOS Y LA CANTIDAD DE ESPACIOS ELIMINADOS
def elimina_espacios (string):
  stringf = ""
  nespacios = 0
  for elemento in string:                  #VERIFICAR SI HAY ESPACIOS EN BLANCO EN EL STRING
      if elemento == " ":
          nespacios =  nespacios + 1       #SUMAR EL NÚMERO DE ESPACIOS QUE HAY EN EL STRING
      else:
          stringf = stringf + elemento
  return stringf, nespacios



#EJERCICIO3
#RECIBE DOS TUPLAS Y RETORNA UNA LISTA DE LAS TUPLAS DE ENTRADA Y LA CANTIDAD DE VECES QUE SE REPITE
#ENTRADA: 2 TUPLAS
#SALIDA: cada palabra de la tupla de palabras de entrada y la cantidad de veces que aparece
def cuenta_palabras(tupla1,tupla2):
    lista = []
    for elemento1 in tupla1:
        contador = 0
        for elemento2 in tupla2:
            contador += elemento2.count(elemento1)
        lista.append((elemento1, contador))
    return lista



#EJERCICIO 4
#RECIBE UN DIGITO QUE REPRESENTA LA CANTIDAD DE TÉRMINO DE LA FUNCIÓN FIBONACCI Y RETORNA TODOS LOS TÉRMINOS
#ENTRADA: UN DIGITO
#SALIDA: UNA LISTA
def fibonacci(n):
    n1 = 0                   #PRIMER TÉRMINO
    n2 = 1                   #SEGUNDO TÉRMINO
    contador = 0
    lista = [n1,n2]
    while contador < n:      #SE CICLA HASTA LLEGAR AL NÚMERO DE TÉRMINOS
        nf = n1 + n2         #NÚMERO FIBONACCI ES LA SUMA DEL PRIMER Y SEGUNDO TÉRMINO
        lista.append (nf)    #SE AGREGA A LA LISTA EL NÚMERO FIBONACCI
        n1 = n2
        n2 = nf
        contador += 1
    return lista



# EJERCICIO 5
# RECIBA TRES NÚMERO NATURALES E IMPRIME LA TABLA DE MULTIPLICAR DEL PRIMER VALOR EMPEZANDO EN EL SEGUNDO VALOR Y TERMINANDO EN EL TERCER VALIR
# ENTRADAS: TRES DIGITOS
# SALIDAS: RESULTADO DE LAS TABLAS
def tabla_multiplicar():
    n = int(input("Tabla de multiplicar del número: "))
    inicio = int(input("Empieza en el número: "))
    fin = int(input("Termina en el número: "))

    for inicio in range(inicio, fin + 1):
        print(n, "x", inicio, "=", n * inicio)


#EJERCICIO6
#RECIBE UN STRING Y RETORNA UN BOOLEANO SEGUN SI LA PALABRA ES PALINDROMA O NO
#ENTRADA: UN STRING
#SALIDA: VALOR BOOLEANO
def es_palabra_palindroma(string):
    indice=-1
    inversa=''
    for letra in string:
        caracter = string[indice]
        inversa = inversa + caracter
        indice-=1
    if inversa == string:
        return True
    else:
        return False



#EJERCICIO7
# tarea ejercicio 7
def decimal_a_binario(lista):
    contador = 0
    lista_binaria = []
    numero_binario = []

    while contador < len(lista):
        numero_binario.clear()
        numero = lista[contador]
        if numero <= 0:
            print("numero no valido")
            break
        else:
            while numero != 1:
                if numero % 2 != 0:
                    residuo = numero % 2
                    numero = numero - 1
                    numero = numero / 2
                    numero_binario.append(residuo)
                else:
                    residuo = numero % 2
                    numero = numero / 2
                    numero_binario.append(residuo)
            numero_binario.append(1)
            # [0, 0, 1]
            # [1, 0 , 0]
            binario = 0
            contador2 = 0
            for i in numero_binario:
                binario = binario + (i * (10 ** contador2))
                contador2 = contador2 + 1
            lista_binaria.append(binario)
            contador = contador + 1
    return lista_binaria



#EJERCICIO8
def lista_cercanos(lista):
    cercanos = []
    for tupla in lista:

        n_numero = tupla[-1]
        resta2 = 10000
        for j in tupla[:-1]:

            resta = n_numero - j

            if resta < 0:
                resta = 0 - resta

            if resta < resta2:
                resta2 = resta
                numero_cercano = j

            if resta == resta2:
                numero_cercano = min(numero_cercano, j)

        cercanos.append((n_numero, numero_cercano))

    return cercanos



#EJERCICIO9
#RECIBE UN NUMERO N Y RETORNA EL FACTORIAL DE N
#ENTRADA: NUMERO NATURAL MAYOR O IGUAL A 0
#SALIDA: EL PRODUCTO DE TODOS LOS NUMEROS DE 1 HASTA EL NUMERO DE ENTRADA
def factorial(numero):
    if numero < 0: #RESTRICCION
        return 0
    rango = numero + 1
    factorial = 1
    for elemento in range(1,rango):
        factorial = factorial * (elemento)
    return factorial
print(factorial(0))



#EJERCICIO10
def combinatoria(n, x):
    denominador = factorial(n)
    numerador = factorial(x) * factorial(n - x)
    resultado = denominador / numerador
    return resultado
def factorial(numero):
    x = 1
    if numero == 0:
        return 1
    else:
        for i in range(1, numero + 1):
            x = x * i
        return x
def factorial_reutilizable(numero):
    if numero == 0 or numero == 1:
        factorial = 1
    else:
        factorial = numero * factorial_reutilizable(numero - 1)
    return factorial



#EJERCICIO11
def numeros_bonitos(cantidad):
    if cantidad < 1:
        print("No valido")
    else:
        lista = []
        contador = 0
        numero = 1
        while contador < cantidad:
            if verificar_numeros_bonitos(numero) == True:
                lista.append(numero)
                contador = contador + 1
            numero = numero + 1
        return lista

def verificar_numeros_bonitos(numero):
    if numero < 10:
        suma = numero
    else:
        suma = suma_de_digitos(numero)
    formula = 3 * numero + 11
    if (suma == suma_de_digitos(formula)):
        bonito = True
        return bonito
    else:
        bonito = False
        return bonito

def suma_de_digitos(numero):
    suma = 0
    tmp = 0
    while numero != 0:
        tmp = numero % 10
        numero = numero // 10
        suma = suma + tmp
    return suma



#EJERCICIO12
#RECIBE UNA LISTA EN UN FORMATO Y RETORNA OTRA LISTA CON LOS DATOS DISTRIBUIDOS DE UNA MANERA DISTINTA
#ENTRADA: LISTA ORDENADA SEGUN LAS MATERIAS
#SALIDA: LISTA ORDENADA SEGUN CARNES
def estudiantes_y_materias(entrada):
    alumnos = []  # lISTA PARA LAS CALIFICACIONES
    for list_cursos in entrada:  # CADA ELEMENTO ES UNA LISTA DE "CALIFICACIONES"
        for tuple_notas in list_cursos[1:]:  # SE UTILIZA TROZOS DEL INDICE 1 HASTA EL FINAL DE CADA TUPLA DE MATERIAS
            factor = -1
            for indice, lista_estudiante in enumerate(alumnos):  #POR CADA ITERACION SE OBTIENE INDICE Y ELEMENTO
                if tuple_notas[0] == lista_estudiante[0]:  #VERIFICACIÓN DE EXISTENCIA
                    factor = indice
                    break

            if factor == -1:  #EN CASO DE QUE EL CARNE NO EXISTA SE AÑADE JUNTO LA MATERIA CON SU RESPECTIA NOTA
                alumnos.append([tuple_notas[0], tuple_notas[1], (tuple_notas[2], list_cursos[0])])
            else:  #SI YA EXISTE EL CARNE SE AÑADE SOLAMENTE LA MATERIA CON SU RESPECTIVA NOTA
                alumnos[factor].append((tuple_notas[2], list_cursos[0]))
    return alumnos
