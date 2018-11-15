# Alex Fernando Leyva Martinez - A01747078 - GRUPO 04
# Este programa permite poner en práctica los usos de listas con distintos tipos de ejercicios.


# Regresa una lista con los valores pares de la lista original
def extraerPares(listaNumeros):
    listaPares = []
    for k in (listaNumeros):
        if k % 2 == 0:
            listaPares.append(k)

    return listaPares


# Regresa una lista con los valores que son mayores a un elemento previo
def extraerMayoresPrevio(listaNumeros):
    listaMayores = []
    for k in range(1, len(listaNumeros)):
        if listaNumeros[k] > listaNumeros[k-1]:
            listaMayores.append(listaNumeros[k])

    return listaMayores


# Regresa una lista con cada pareja de datos intercambiada
def intercambiarParejas(listaNumeros):
    listaParejas = []
    for k in range(1,len(listaNumeros),2):
        listaParejas.append(listaNumeros[k])
        listaParejas.append(listaNumeros[k-1])
    if len(listaNumeros) % 2:
        listaParejas.append(listaNumeros[-1])

    return listaParejas


#  Recibe una lista y la modifica otercambiando el valor menor y mayor
def intercambiarMM(listaNumeros):
    if len(listaNumeros) != []:
        mayor = list.index(listaNumeros, max(listaNumeros))
        menor = list.index(listaNumeros, min(listaNumeros))
        listaNumeros[mayor], listaNumeros[menor] = listaNumeros[menor], listaNumeros[mayor]

    return listaNumeros


# Regresa el promedio centro de los valores, es decir sin considerar el valor mayor y el menor
def promediarCentro(listaNumeros):
    listaNumeros.sort()
    lista = listaNumeros[1:len(listaNumeros)-1]
    if sum(lista) > 0:
        promedio = sum(lista)//len(lista)
        return promedio
    else:
        return 0


# Recibe una lista de números y regresa una dupla con la media y la desviación estándar
def calcularEstadistica(listaNumeros):
    n = len(listaNumeros)
    if n != 0:
        suma = sum(listaNumeros)
        media = suma / n
    else:
        media = 0
    if n > 1:
        suma = 0
        for k in listaNumeros:
            suma += (k - media)**2
        desviacion = (suma/(n-1))**0.5
    else:
        desviacion = 0

    dupla = (media, desviacion)
    return dupla


# Recibe una lista y regresa la suma de los valores de la lista sin contar aquellos que estén al lado de un 13
def calcularSuma(listaNumeros):
    if 13 not in listaNumeros:
       return sum(listaNumeros)
    else:
        for k in range(len(listaNumeros)):
            if listaNumeros[k] == 13:
                if k != 0:
                    listaNumeros[k-1] = False
                listaNumeros[k] = False
                if k != len(listaNumeros):
                    listaNumeros[k+1] = False
        while False in listaNumeros:
            listaNumeros.remove(False)
        return sum(listaNumeros)
