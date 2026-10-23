

def Config_A (c):
    falha = (1 - ((1 - c[0])*(1 - c[1]))) * (1 - ((1 - c[2]) * (1 - c[3])))
    return 1 - falha

def Config_B (c):
    falha = (1 - (c[0] * c[2])) * (1 - (c[1] * c[3]))
    return falha


c = []
for i in range (4):
    c.append(float(input(f'Taxa de fracasso do componente {1+i} (0-1) para um sistema de 4 componentes: ')))
    
if any(n > 1 or n < 0 for n in c):
        print('Todos os componentes precisam estar entre 0 e 1 em taxa de fracasso!')
    
else:    
    print()
    config = (input('Escolha entre a configuração A e B (digite A ou B): ')).upper()
        
    while config not in ('A', 'B'):
        config = input('Escolha entre a configuração A e B (digite A ou B): ').upper()
        
    if config == 'A':
        sucesso = Config_A (c)
        
    elif config == 'B':
        sucesso = Config_B (c)

    print ()
    print (f'A taxa de sucesso é {100*sucesso:.2f}%')