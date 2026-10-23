import sys

n = int(input('Quantidade de soluções independentes: '))

if n < 1:
    print()
    print('Deve ter pelo menos 1 tentativa de solução!')

else:
    
    tent=0
    tentf = 1
    
    for i in range (n):
        tent = (float(input(f'Chance de sucesso da {i+1} tentativa (entre 0-1): ')))
        
        if tent > 1 or tent < 0:
            print()
            print ('Chance de sucesso deve ser entre 0 e 1!')
            sys.exit()
        
        else:
            tentf = (1 - tent) * tentf
    
    print()   
    print (f'Tem {100*(1 - tentf):.2f}% de chance de resolver o problema')
    