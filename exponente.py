base=int(input("base? "))
exponente=int(input("exponente? "))

contador=0
resultado=1

while contador < exponente:    
    resultado = resultado * base
    contador = contador + 1
print(resultado)
