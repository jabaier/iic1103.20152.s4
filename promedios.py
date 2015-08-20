N=int(input("cuantos numeros promediaremos? "))

if N > 0:
    contador = 0
    suma = 0

    while contador < N:
        numero = int(input("entregame el numero "+str(contador+1)+": "))
        suma = suma + numero
        contador = contador + 1

    promedio = suma/N
    print("el promedio es "+str(promedio))

if N <= 0:
    print("debes ingresar un numero positivo")
