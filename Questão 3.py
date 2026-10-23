
qA = int(input('Quantidade de funcionários da empresa A: '))
qB = int(input('Quantidade de funcionários da empresa B: '))
qC = int(input('Quantidade de funcionários da empresa C: '))
qD = int(input('Quantidade de funcionários da empresa D: '))
qE = int(input('Quantidade de funcionários da empresa E: '))
if qA < 1 or qB < 1 or qC < 1 or qD < 1 or qE < 1:
    print()
    print('Todas as empresas precisam ao menos 1 funcionário!')

else:
    qT = qA + qB + qC + qD + qE

    pA = qA / qT
    pB = qB / qT
    pC = qC / qT
    pD = qD / qT
    pE = qE / qT
    
    print ()
    print (f'Tem {pA*100:.2f}% de chance de escolher alguém da empresa A')
    print (f'Tem {pB*100:.2f}% de chance de escolher alguém da empresa B')
    print (f'Tem {pC*100:.2f}% de chance de escolher alguém da empresa C')
    print (f'Tem {pD*100:.2f}% de chance de escolher alguém da empresa D')
    print (f'Tem {pE*100:.2f}% de chance de escolher alguém da empresa E')
    print ()
    print (f'Tem {(1 - pA)*100:.2f}% de chance de não escolher a empresa A')
    
#%%

# Método mais genérico que consegui

quant = int(input('Quantidade de empresas a ser contabilizadas: '))

q = []
for i in range (quant):
    q.append(int(input(f'Quantidade de funcionários da empresa {i+1}: ')))
    
qT = sum(q)

if any(n < 1 for n in q):
    print()
    print('Todas as empresas precisam ao menos 1 funcionário!')
else:
    print()
    
    p = []
    for i in range (quant):
        p.append(q[i] / qT)
        
        print (f'Tem {p[i]*100:.2f}% de chance de escolher alguém da Empresa {i+1}')
    
    print()
    qE = int(input(f'Escolha uma empresa para saber a chance de o funcionário não ser dela (1 até {quant}):'))
    while qE < 1 or qE > quant:
        qE = int(input(f'Valor inválido! Escolha uma empresa entre 1 e {quant}: '))
    
    print ()
    print (f'Tem {(1 - p[qE - 1])*100:.2f}% de chance de não escolher a Empresa {qE}')