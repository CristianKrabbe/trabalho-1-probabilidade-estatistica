import math
import sys

def quant_espec (n, p, k):   
    errot = (math.comb(n, k))*(p**k)*((1 - p)**(n-k))
    return errot      

def mais_quant (n, p, k):   
    errot = 0    
    for i in range (k+1, n+1):
            errot += (math.comb(n, i))*(p**i)*((1 - p)**((n)-(i)))
    return errot

def ate_quant (n, p, k):    
    errot = 0
    for i in range (k+1):
            errot += (math.comb(n, i))*(p**i)*((1 - p)**(n-i))
    return errot
        
def algum_erro (n, p):
    k = 0
    errot = (math.comb(n, k))*(p**k)*((1 - p)**(n-k))
    return 1 - errot 


n = int(input('Quantidade total de itens a ser contabilizados: '))
p = float(input('Probabilidade de erro (0-1): '))
print()


if n < 1:
    print('Precisa pelo menos um item!')
elif p > 1 or p < 0:
    print('O erro precisa estar entre 0 e 1!')

else:
    k = 0
    print(f'São esperados {n*p:.2f} item(s) com erro e {n-(n*p):.2f} item(s) sem erro')
    print(f'A variância é {n*p*(1-p):.2f} e o desvio-padrão é {math.sqrt(n*p*(1-p)):.2f} ')
 
    print()
    print('Escolha dentre as seguintes funções:')
    print('A = Probabilidade dessa quantidade específica de itens defeituosos:')
    print('B = Probabilidade de mais que essa quantidade de itens defeituosos:')
    print('C = Probabilidade de até essa quantidade de itens defeituosos:')
    print('D = Probabilidade de algum item defeituoso')
    print('E = Encerrar')
    print()
    func = input('Digite a função escolhida: ').upper()
    
    while func not in ('A', 'B', 'C', 'D', 'E'):
        func = input('Digite a função escolhida: ').upper()
    
    if func in ('A', 'B', 'C'):
        k = int(input('Digite a quantidade: '))
        print()
        if k < 0:
            print('Essa quantidade não pode ser negativa!')
        elif k > n:
            print('Não pode ser mais que o total!')
        else:            
                 
            if func == 'A':
                erro = quant_espec (n, p, k)
                print(f'A probabilidade de {k} itens serem defeituosos é {100*erro:.2f}%')
                
            elif func == 'B':
                erro = mais_quant (n, p, k)
                print(f'A probabilidade de mais de {k} itens serem defeituosos é {100*erro:.2f}%')
                
            elif func == 'C':
                erro = ate_quant (n, p, k) 
                print(f'A probabilidade de até {k} itens serem defeituosos é {100*erro:.2f}%')
                
    else:
            if func == 'D':
                erro = algum_erro (n, p)
                print(f'A probabilidade de algum item ser defeituoso é {100*erro:.2f}%')
                
            else:
                sys.exit()
        
        
     
    

   
    
   
    
   
    

    
    
    
    

        