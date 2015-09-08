def estriangulo(a,b,c):
    return a+b>c and a+c>b and c+b>a

def espitagorico(a,b,c):
    return a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2

def esisosceles(a,b,c):
    return a==b or a==c or b==c

x=float(input("x? "))
y=float(input("y? "))
z=float(input("z? "))

if estriangulo(x,y,z):
    if espitagorico(x,y,z):
        if esisosceles(x,y,z):
            print("El triangulo es recto e isosceles")
        else:
            print("El triangulo es recto")    
    elif esisosceles(x,y,z):
        print("El triangulo es isosceles")
    else:
        print("Es un triangulo")
else:
    print("No es un triangulo")
