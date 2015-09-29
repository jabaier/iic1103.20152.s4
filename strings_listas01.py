
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


v=sumalista_cool([3,4,5])

print(sumalista_cool([3,4,5]))
print(sumalista_cool([1,1,1,1]))
