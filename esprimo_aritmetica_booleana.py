N=int(input("numero? "))


esprimo = (N % 2 != 0)

divisor=3

while divisor <= N**0.5 and esprimo:
#while divisor <= N-1 and esprimo:
    esprimo = esprimo and (N % divisor != 0)
    divisor = divisor + 2

if  esprimo:
    print("el numero es primo")
else:
    print("el numero no es primo")
