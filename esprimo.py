N=int(input("numero? "))
denominador=N-1
esprimo = True

while denominador >= 2:
    resto = N % denominador
    if resto == 0:
        esprimo = False
    denominador = denominador - 1

if  esprimo:
    print("el numero es primo")
else:
    print("el numero no es primo")
