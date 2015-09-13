def es_primo(N):
    esprimo = True
    divisor=2
    while divisor <= N-1 and esprimo:
        esprimo = esprimo and (N % divisor != 0)
        divisor = divisor + 1
    return esprimo

cuantos = int(input('cuantos primos quieres que muestre? '))
N = 2

gemelos = 0 #cuantos primos gemelos hemos impreso en pantalla
while gemelos < cuantos:
    if es_primo(N) and es_primo(N+2):
            print(N,N+2)
            gemelos=gemelos+1
    N = N+1
