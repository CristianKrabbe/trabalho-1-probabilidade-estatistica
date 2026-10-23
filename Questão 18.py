from scipy.stats import norm


def mais_quant (med, dp, k):     
    prob = norm.cdf(k, med, dp)
    return 1 - prob

def ate_quant (med, dp, k):    
   prob = norm.cdf(k, med, dp)
   return prob

def entre (med, dp, k1, k2):
    prob1 = norm.cdf(k1, med, dp)
    prob2 = norm.cdf(k2, med, dp)
    return (prob2 - prob1)


med = 0
dp = 1

print('Escolha dentre as seguintes funções:')
print()
print('A = Probabilidade de ser superior a esse valor:')
print('B = Probabilidade de ser inferiror a esse valor:')
print('C = Probabilidade de estar entre 2 valores:')

print()
func = input('Digite a função escolhida: ').upper()
print()
 
while func not in ('A', 'B', 'C'):
     func = input('Digite a função escolhida: ').upper()
     print()
 
 
if func in ('A', 'B'):
    k = float(input('Digite o valor: '))
    print()
     
    if func == 'A':
        prob = mais_quant (med, dp, k)
        print(f'A probabilidade de ser mais que {k} é {100*prob:.2f}%')
         
    elif func == 'B':
        prob = ate_quant (med, dp, k)
        print(f'A probabilidade de ser menos que {k} é {100*prob:.2f}%')
else:
     k1 = float(input('Coloque o limite inferior: '))
     k2 = float(input('Coloque o limite superior: '))
     print()
     
     if k1 > k2:
         print('O limite inferior não pode ser maior que o limite superior!')
     else:
         prob = entre (med, dp, k1, k2)
         print(f'A probabilidade de estar entre {k1} e {k2} é {100*prob:.2f}%')