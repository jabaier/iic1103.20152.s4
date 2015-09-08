def estriangulo(a,b,c):
    print("el primer argumento es:",a)
    print("el segundo argumento es:",b)
    print("el tercer argumento es:",c)
    return a+b>c and a+c>b and c+b>a

def espitagorico(a,b,c):
    return a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2

def esisosceles(a,b,c):
    return a==b or a==c or b==c

print(estriangulo(int(input("numero? ")),4,5))
print(espitagorico(3,4,5))
print(esisosceles(3,4,5))
