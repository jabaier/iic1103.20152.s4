cuantos = int(input('cuantos primos quieres que muestre? '))

N = 2

gemelos = 0 #cuantos primos gemelos hemos impreso en pantalla

while gemelos < cuantos:
    esprimo = True
    divisor=2
    while divisor <= N-1 and esprimo:
        #while divisor <= N-1 and esprimo:
        esprimo = esprimo and (N % divisor != 0)
        divisor = divisor + 1
    if  esprimo:
        esgemelo = True
        divisor=2
        while divisor <= (N+2)-1 and esgemelo:
            #while divisor <= N-1 and esprimo:
            esgemelo = esgemelo and ( (N+2) % divisor != 0)
            divisor = divisor + 1

        if esgemelo:
            print(N,N+2)
            gemelos=gemelos+1
    N = N+1
    
