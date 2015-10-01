
def sumalista(l):
    i=0
    suma=0
    while i < len(l):
        suma = suma + l[i]
        i = i + 1
    return suma

def sumalista_cool(l):
    suma = 0
    for elemento in l:
        suma = suma + elemento
    return suma

def desafio_google(l):
    i = 0
    while i < len(l):
        if sumalista(l[:i]) == sumalista(l[i+1:]):
            return i
        i = i + 1
    return -1

def mayusculas():
    i = ord('A')
    fin = ord('Z')
    mayusculas = ''
    while i <= fin:
        mayusculas = mayusculas + chr(i)
        i = i + 1
    return mayusculas

def minusculas():
    return mayusculas().lower()


def rot_encriptacion(mensaje, incremento):
    M = mayusculas()
    m = minusculas()
    mensaje_encriptado=''
    for c in mensaje:
        indiceM = M.find(c)
        indicem = m.find(c)
        if indiceM >= 0:         # es mayuscula
            caracter = M[(indiceM+incremento)%26]
        elif indicem >= 0:
            caracter = m[(indicem+incremento)%26]
        else:
            caracter = c
        mensaje_encriptado = mensaje_encriptado + caracter
    return mensaje_encriptado

enc = rot_encriptacion("Este es un Mensaje muy secreto",13)
desenc = rot_encriptacion(enc,13)
print(enc)
print(desenc)
