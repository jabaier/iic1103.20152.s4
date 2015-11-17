
def subsecuencia(L):
    if L==[]:
        return [[]]
    R=subsecuencia(L[1:])
    S=[[L[0]]+r for r in R]
#    S=[]
#    for r in R:
#        S.append([L[0]]+r)
    return S+R

print(subsecuencia([1,2,3,4,5]))
