cuantos = int(input('cuantos primos gemelos quieres que muestre? '))

def esprimo(N):
    esprimo = True
    divisor=2
    while divisor <= N-1 and esprimo:
        #while divisor <= N-1 and esprimo:
        esprimo = esprimo and (N % divisor != 0)
        divisor = divisor + 1
    return esprimo

N = 2

gemelos = 0 #cuantos primos gemelos hemos impreso en pantalla

while gemelos < cuantos:
    if esprimo(N) and esprimo(N+2):
            print(N,N+2)
            gemelos=gemelos+1
    N=N+1
    
