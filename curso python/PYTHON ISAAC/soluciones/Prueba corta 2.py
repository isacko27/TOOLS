##########################
## Aarón Salas Alvarado ##
##########################

def imprimir_palindromos(numero):
    if not isinstance(numero, int):              #RESTRICCIONES
        return "Debe ser un numero entero"
    if numero < 1:                               #RESTRICCIONES
        return "Debe ser un numero mayor o igual a 1"
    else:
        contador = 1
        palindromos = 0
        print("Cantidad de palindromos a imprimir:", numero)
        while contador <= numero:                             #Ciclo

            if palindromos < 10:                              #VERIFICACION DE NUMEROS MENORES A 10
                if palindromos == palindromos:
                    print(contador, palindromos)
                    contador = contador + 1

            if 9 < palindromos < 100:                         #VERIFICACION DE NUMEROS DE 2 DIGITOS
                unidades = palindromos % 10
                decenas = palindromos // 10
                inverso = unidades * 10 + decenas
                if inverso == palindromos:
                    print(contador, palindromos)
                    contador = contador + 1

            if 99 < palindromos < 1000:                       #VERIFICACION DE NUMEROS DE 3 DIGITOS
                unidades = palindromos % 10
                decenas = palindromos % 100 // 10
                centenas = palindromos // 100
                inverso = unidades * 100 + decenas * 10 + centenas
                if inverso == palindromos:
                    print(contador, palindromos)
                    palindromos = palindromos + 1
                    contador = contador + 1
                else:
                    palindromos = palindromos + 1
            else:
                palindromos = palindromos + 1



def determinar_numeros_amistosos(numero1, numero2):
    divisor = 1
    divisor2 = 1
    amistad1 = 0
    amistad2 = 0

    if numero1 == numero2:
        return "LAS ENTRADAS DEBEN SER NÚMEROS DIFERENTES"         #RESTRICCIONES
    if not isinstance(numero1 and numero2, int):
        return "LAS ENTRADAS DEBEN SER NÚMEROS NATURALES >= 2"     #RESTRICCIONES
    if numero1 and numero2 <= 2:
        return "LAS ENTRADAS DEBEN SER NÚMEROS NATURALES >= 2"     #RESTRICCIONES

    while divisor < numero1 - 1:                          #CICLO
        factor = numero1 / divisor
        if factor%1 == 0:
            amistad1 = divisor + amistad1
            divisor = divisor + 1
        else:
            divisor = divisor + 1

    while divisor2 < numero2 - 1:                          #CICLO
        factor2 = numero2 / divisor2
        if factor2%1 == 0:
            amistad2 = divisor2 + amistad2
            divisor2 = divisor2 + 1
        else:
            divisor2 = divisor2 + 1

    if amistad1 == numero2 and amistad2 == numero1:                            #RETORNAR TRUE O FALSE SEGUN RESULTADOS
        return True
    else:
        return False