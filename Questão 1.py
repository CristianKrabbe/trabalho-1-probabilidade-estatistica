
def Uniao (A, B):
    A = map(float, A)
    B = map(float, B)
    U = sorted(set(A).union(set(B)))
    return U

def Intersec (A, B):
    A = map(float, A)
    B = map(float, B)
    I = sorted(set(A).intersection(set(B)))
    return I

def Complement (A, Uni):
    A = set(map(float, A))
    Uni = set(map(float, Uni))
    Ac = sorted(set(Uni).difference(set(A)))
    return Ac
    

A = input('Conjunto A: ').split()
B = input('Conjunto B: ').split()
C = input('Conjunto C: ').split()

Uni = set(map(float, A)).union(set(map(float, B))).union(set(map(float, C)))

resp1 = Uniao (A, B)
resp2 = Intersec (A, B)
resp3 = Intersec (A, C)
resp4 = Complement (A, Uni)


print (f'A união de A e B é {resp1}')
print (f'A intersecção de A e B é {resp2}')
print (f'A intersecção de A e C é {resp3}')
print (f'A complementar de A é {resp4}')