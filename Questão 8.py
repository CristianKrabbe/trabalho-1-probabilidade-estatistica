import math

quant = int(input('Quantidade de empresas a ser contabilizadas: '))
print()

if quant < 1:
    print('Precisa pelo menos uma empresa!')

else:
    
    p = []
    perro = []
    
    for i in range (quant):
        p.append(float(input(f'Porcentagem da produção/processamento referente a empresa {i+1} (0-1): ')))
        perro.append(float(input(f'Porcentagem do erro/falha referente a empresa {i+1} (0-1): ')))
        print()
        
    if any(n > 1 or n < 0 for n in p):
        print('Todas empresas precisam estar entre 0 e 1 em processamento/produção!')
        
    elif any(n > 1 or n < 0 for n in perro):
        print('O erro deve estar entre >/= 0 e 1!')
        
    elif not math.isclose(sum(p), 1):
        print('A soma de toda a produção/processamento deve ser igual a 1!')
    
    else:
    
        errorel = []
        for i in range (quant):
            errorel.append(p[i]*perro[i])
        
        errot = sum(errorel)

        print()
        print(f'O probabilidade de erro total é {(100*errot):.2f}%')
        print()
    
        if errot == 0:
            print('Não é possível calcular a probalidade de erro relativo de uma empresa específica (erro total = 0)!')
            
        else:
            
            for i in range (quant):
                print(f'A chance do erro ser da empresa {1+i} é {(100*(errorel[i]/errot)):.2f}%')