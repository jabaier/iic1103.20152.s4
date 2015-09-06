cuantos = int(input('cuantos primos quieres que muestre? '))

N = 2

primos = 0 #cuantos primos hemos impreso en pantalla

while primos < cuantos:
    esprimo = True
    divisor=2
    while divisor <= N-1 and esprimo:
            #while divisor <= N-1 and esprimo:
            esprimo = esprimo and (N % divisor != 0)
            divisor = divisor + 1
    if  esprimo:
        print(N)
        primos=primos+1
    N = N + 1
