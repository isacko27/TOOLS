###########################################################################
###  TAREA 5: PRÁCTICA MATRICES, DICCIONARIOS, LISTAS, TUPLAS, STRINGS  ###
###  Autor: Aarón Salas Alvarado(2022437501)                            ###
###  Coautores: Samuel Gomez Villanueva y Pamela Rojas                  ###
###########################################################################
#EJERCICIO 3
#Recibe un entero n (>=1) e imprime los primeros n números bonitos
def numeros_bonitos(numero):
    contador = 0                                 # CONTADOR PARA DESCOMPONER CIFRAS EN SUS DIGITOS
    count1 = 0                                   # CONTADOR DE NUMEROS BONITOS ENCONTRADOS

    while count1 <= numero - 1:                  # CICLADO DE 1 A N QUE DETERMINA LOS NUMEROS BONITOS EN ESE RANGO
        contador1 = contador                     # SEREPLICA EL CONTADOR PARA CREAR UN CICLO DE DESCOMPOSICION
        dig1 = int(0)
        suma1 = 0
        while (contador1 != 0):                  #CICLO DE DESCOMPOSICIÓN DE NUMERO EN RANGO
            dig1 = int(contador1 % 10)
            suma1 += dig1
            contador1 = int(contador1 / 10)

        contador2 = 3 * contador + 11            # NUMERO FORMULADO
        dig2 = int(0)
        suma2 = 0
        while (contador2 != 0):                  # CICLO DE DESCOMPOSICIÓN DE RESULTADO DE LA FORMULA
            dig2 = int(contador2 % 10)
            suma2 += dig2
            contador2 = int(contador2 / 10)

        if suma1==suma2:                         # CONDICIONAL PARA DETERMINAR SI SON BONITOS
            count1 = count1 + 1                  # AUMENTA CONTADOR DE NUMEROS BONITOS ENCONTRADOS
            print(count1,")", contador)          # IMPRESION EN EL FORMATO INDICADO
        contador = contador + 1                  # AUMENTA EL CONTADOR GENERAL



#EJERCICIO 6
#RECIBE UN RANGO DE NUM1 A NUM2 Y RETORNA TODOS LOS NUMERO SEMIPRIMOS Y SUS COMPONENTES PRIMOS

def primo(entrada):                                           # FUNCION BOOLEANA PARA DETERMINAR PRIMOS
    if entrada % 1 != 0:
        return False
    divisor = 2
    raiz = int(entrada**(0.5))
    while divisor<=raiz:
        if entrada%divisor == 0:
            return False
        divisor+=1
    return True

def semiprimos(num1, num2):
    print("Semiprimos      Primos que lo conforman")
    contadorprimos = 0                                        # CONTADOR DE NUEROS PRIMOS
    for elemento in range((abs(num1)), (abs(num2)+1)):        # SE DETERMINA RANGO DE NUM1 A NUM2
        if primo(elemento)==False:                            # SI ELEMENTO EN RANGO NO ES PRIMO, PUEDES SER SEMIPRIMO
            for subelemento in range(1, elemento):            # SE CRE UN RANGO DE CERO A ELEMENTO
                if primo(subelemento) == True:                # SI ALGUN SUBELEMENTO ES PRIMO, LO USAMOS EN LA LOGICA
                    division = elemento / subelemento         # INTENTAMOS DESCOMPONER EL NUMERO
                    if primo(division) == True:               # SI EL RESULTADO DE LA DESCOMPOSICIÓN ES PRIMO ENTONCES ESTAMOS ANTE UN SEMIPRIMO Y SUS COMPONENTES PRIMOS
                        print("   ", elemento, "                 ", subelemento,"x", int(division))
                        contadorprimos=contadorprimos + 1     # CONTADOR DE NUMERO SEMIPRIMOS DETERMINADOS
                        break                                 # SE FINALIZA EL CICLO DE DETERMINACION DE ELEMENTO EN RANGO
    print("Cantidad de semiprimos: ", contadorprimos)
print(semiprimos(14, 24))





#EJERCICIO 8
#RECIBE UN DICCIONARIO CON UN FORMATO Y RETORNA OTRO DICCIONARIO CON OTRO FORMATO
def materias(diccionario):
    formato = {}                                  # DICCIONARIO PARA LAS CALIFICACIONES
    for carnet in diccionario:                    # SE ANALIZA CANET POR CARNET
        for materia in diccionario[carnet][1:]:   # INGRESAMOS LOS DATOS DE CADA ESTUDIANTE
            if materia[1] in formato:             # CONDICIONAL PARA EXCLUIR REPETICIONES
                formato[materia[1]] = formato[materia[1]] + [(carnet, diccionario[carnet][0], materia[0]), ]
            else:
                formato[materia[1]] = [(carnet, diccionario[carnet][0], materia[0]),]
    return formato






