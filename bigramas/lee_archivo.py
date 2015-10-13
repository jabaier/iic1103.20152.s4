
def sin_puntuacion(palabra):
    puntuacion=",.!¡?¿:;"
    resp = ""
    for c in palabra:
        if not c in puntuacion:
            resp = resp + c
    return resp

nombre_archivo=input("ingrese el nombre del archivo: ")

f = open(nombre_archivo,"r")

entrada=''
for linea in f:
    entrada = entrada + linea

f.close()

palabras = entrada.split()

palabras2 = []
for p in palabras:
    pal = sin_puntuacion(p)
    if pal != "":
        palabras2.append(pal.lower())

print(palabras2)
