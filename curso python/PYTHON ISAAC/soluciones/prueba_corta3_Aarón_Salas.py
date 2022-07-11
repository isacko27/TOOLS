########################################################
#### Aarón David Salas Alvarado #### PRUEBA CORTA 4 ####
########################################################

#EJERCCIO 1
#RECIBE  DOS NÚMERO E IMPRIME LOS NÚMEROS QUE SON ABUNDANTES EN UN RANGO DEL PRIMER NUMERO AL SEGUNDO NUMERO
#ENTRADAS: DOS NÚMEROS
#SALIDAS: UNA LISTA DE LOS NUMEROS ABUNDANTES DENTRO DEL RANGO Y SUS DIVISORES
def numero_abundantes_en_rango(num1, num2):
    if num1 >= num2:                              #RESTRICCION
        return []
    if num1%1 or num2%1 != 0:                     #RESTRICCION
        return []
    lista = []                                    #"lista" ALMACENA LAS RESPECTIVAS LISTAS DE CADA NUMERO ABUNDANTE
    for elemento in range(abs(num1), abs(num2)):  #SE CREA UN CICLO QUE ANALIZA NUMEROS DESDE EL ENOR AL MAYOR NUMERO
        contador = 1                              #"contador" SE USA EN EL WHILE Y COMO DIVISOR
        sumadivisores = 0                         #SUMA DE DIVISORES DE n PARA DETERMINAR SI ES MAYOR A nx2
        divisores = [elemento]                    #LISTA DE NUMERO ABUNDANTE Y DIVISORES
        while contador<=elemento:                 #CICLO QUE DETERMINA
            if elemento%contador == 0:
                divisores.append(contador)
                sumadivisores = sumadivisores + contador
            contador = contador + 1
        if sumadivisores > elemento*2:
            lista.append(divisores)
    return lista
print(numero_abundantes_en_rango(12, 30))

#EJERCICIO 2
#RECIBE UN STRING COMO CONTRASEÑA Y LO VALIDA SEGUN LAS RESTRICCIONES
#LOS CARACTERES SE CLASIFICAN EN CATEGORIAS 1, 2, 3 Y 4
def validar_contraseña(contraseña):
    if not isinstance(contraseña, str):            #RESTRICCIÓN DE NUMEROS ENTEROS
        return 9
    categoria1="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"       #SIGNOS DE CATEGORIA 1
    categoria2= "abcdefghijklmnñopqrstuvwxyz"      #SIGNOS DE CATEGORIA 2
    categoria3= "0123456789"                       #SIGNOS DE CATEGORIA 3
    cat1=0                                         #CONTADOR DE SIGNOS DE CATEGORIA 1
    cat2=0                                         #CONTADOR DE SIGNOS DE CATEGORIA 2
    cat3=0                                         #CONTADOR DE SIGNOS DE CATEGORIA 3
    cat4=0                                         #CONTADOR DE SIGNOS DE CATEGORIA 4
    factor = ["0"]                                 #"factor" DETERMINA SI HAY NUMEROS DE LA MISMA CATEGORIA JUNTOS
    for elemento in contraseña:                    #CICLO QUE DETERMINA LA VALIDEZ DE LA CONTRASEÑA Y RESTRICCIONES
        if elemento in categoria1:
            if factor == ["1"]:
                return 5
            factor[0] = "1"
            cat1 = cat1 + 1

        elif elemento in categoria2:
            if factor == ["2"]:
                return 5
            factor[0] = "2"
            cat2 = cat2 + 1

        elif elemento in categoria3:
            if factor == ["3"]:
                return 5
            factor[0] = "3"
            cat3 = cat3 + 1

        else:
            if factor == ["4"]:
                return 5
            factor[0] = "4"
            cat4 = cat4 + 1

    if cat1<2:                   #RESTRICCIONES: MAS DE 2 CARACTERES DE LA MISMA CATEGORIA POR CONTRASEÑA
        return 1
    if cat2<2:
        return 2
    if cat3<2:
        return 3
    if cat4<2:
        return 4

    return 0                   #CONTRASEÑA VALIDA
