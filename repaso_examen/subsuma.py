
def subsuma_exacta(sol,L,S,i):
    if S==0:
        print(sol)
        return False # originalmente True
    if S<0 or L==[]:
        return False
    sol[i]=1  # incluyo al primer numero
    if subsuma_exacta(sol,L[1:],S-L[0],i+1):
        return True
    sol[i]=0  # incluyo al primer numero
    if subsuma_exacta(sol,L[1:],S,i+1):
        return True
    return False

def subsuma_menorigual(sol,L,S,i):
    if S>=0 and L==[]:
        print(sol)
    if S<0 or L==[]:
        return False
    sol[i]=1  # incluyo al primer numero
    subsuma_menorigual(sol,L[1:],S-L[0],i+1)
    sol[i]=0  # incluyo al primer numero
    subsuma_menorigual(sol,L[1:],S,i+1)

def subsuma_menorigual2(sol,L,S,i):
    if S>=0 and L==[]:
        print(sol)
    if S<0 or L==[]:
        return False
    sol2=sol+[L[0]]
    subsuma_menorigual2(sol2,L[1:],S-L[0],i+1)
    subsuma_menorigual2(sol,L[1:],S,i+1)

def encontrar_exacta(L,S):
    sol=[0]*len(L)
    subsuma_exacta(sol,L,S,0)

def encontrar_menorigual(L,S):
    sol=[0]*len(L)
    subsuma_menorigual(sol,L,S,0)

def encontrar_menorigual2(L,S):
    subsuma_menorigual2([],L,S,0)

encontrar_menorigual2([1,2,4,3],5)
