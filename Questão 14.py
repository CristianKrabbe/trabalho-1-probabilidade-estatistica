import math

def quant_espec (med, k):   
    errot = (math.exp(-med)*(med**k))/math.factorial(k)
    return errot      

def mais_quant (med, k):   
    errot = 0    
    for i in range (k+1):
            errot += (math.exp(-med)*(med**i))/math.factorial(i)
    return 1 - errot

def ate_quant (med, k):    
    errot = 0
    for i in range (k+1):
            errot += (math.exp(-med)*(med**i))/math.factorial(i)
    return errot
        
def algum_erro (med):
    k = 0
    errot = (math.exp(-med)*(med**k))/math.factorial(k)
    return 1 - errot

erro = float(input('Probabilidade de erro (0-1): '))
tent = int(input('Quantidade de tentativas idependentes: '))

if erro > 1 or erro < 0:
    print('O erro deve estar entre 0 e 1!')
elif tent < 1:
    print('As tentativas precisam ser pelo menos 1!')

else:   
    med = erro*tent
       
    print()
    print('Escolha dentre as seguintes funções:')
    print('A = Probabilidade dessa quantidade específica de erros:')
    print('B = Probabilidade de mais que essa quantidade de erros:')
    print('C = Probabilidade de até essa quantidade de itens erros:')
    print('D = Probabilidade de algum erro:')
    print()
    func = input('Digite a função escolhida: ').upper()
    
    
    while func not in ('A', 'B', 'C', 'D'):
        func = input('Digite a função escolhida: ').upper()
    
    if func in ('A', 'B', 'C'):
        k = int(input('Digite a quantidade: '))
        print()
        if k < 0:
            print('Essa quantidade não pode ser negativa!')
        elif k > tent:
            print('Não pode ser mais que o total!')
        else:            
     
                
            if func == 'A':
                prob = quant_espec (med, k)
                print(f'A probabilidade de {k} erros ocorrerem é {100*prob:.2f}%')
                
            elif func == 'B':
                prob = mais_quant (med, k)
                print(f'A probabilidade de mais de {k} erros ocorrerem é {100*prob:.2f}%')
                
            elif func == 'C':
                prob = ate_quant (med, k) 
                print(f'A probabilidade de até {k} erros ocorrerem é {100*prob:.2f}%')
                
    else:
            if func == 'D':
                prob = algum_erro (med)
                print(f'A probabilidade de algum erro ocorrer é {100*prob:.2f}%')