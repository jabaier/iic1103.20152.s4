
contador = 0 # cuenta cuantas veces se ha ejecutado el cuerpo del while de abajo
suma = 0
numero = int(input("entregame el numero "+str(contador+1)+": "))
suma = suma + numero

#numero=0

while numero != -1:
    numero = int(input("entregame el numero "+str(contador+2)+": "))
    suma = suma + numero
    contador = contador + 1

if contador == 0:
    print("debes ingresar al menos un numero")
else:
    promedio = (suma+1)/contador
    print("el promedio es "+str(promedio))
