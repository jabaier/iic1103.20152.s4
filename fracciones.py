def mcd(a,b):
    div = min(a,b) # retorna el minimo entre a y b
    while div > 1 and (a%div!=0 or b%div!=0):
        div = div - 1
    return div

class fraccion:
    def __init__(self,numerador=0,denominador=1):
        den=abs(denominador)
        num=abs(numerador)
        MCD=mcd(num,den)
        self.denominador = den // MCD
        if denominador < 0:
            numerador = -numerador
        self.numerador = numerador // MCD

    def __str__(self):
        return str(self.numerador)+"/"+str(self.denominador)

    def __add__(self,frac):
#        print("self vale: ",self)
#        print("f vale: ",frac)
        numerador = self.numerador*frac.denominador+frac.numerador*self.denominador
        denominador = self.denominador*frac.denominador
        return fraccion(numerador,denominador)

    def __radd__(self,x):
        frac=fraccion(x)
        return self+frac

#        numerador = self.numerador*frac.denominador+frac.numerador*self.denominador
#        denominador = self.denominador*frac.denominador
#        return fraccion(numerador,denominador)


f1 = fraccion(2,-5)
f2 = fraccion(10,15)
f3 = f1 + f2
print(f3)
f4 = 1 + f2
print(f4)
