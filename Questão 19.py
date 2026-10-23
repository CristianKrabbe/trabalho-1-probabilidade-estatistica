
# O código da questão 17 já resove esse mesmo problema, então só copiei para cá
# Inclusive na 18 só foi fixado a média e o desvio-padrão e o resto está igual também 

import numpy as np
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

def print_med_e_dp (med, dp):
    print(f'A média é {med:.2f}')
    print(f'O desvio-padrão é {dp:.2f}')


quant = int(input('Quantidade de itens a ser contabilizados: '))
print()

if quant < 1:
    print('Precisa pelo menos um item!')

else:
    med = []
    dp = []
    
    for i in range (quant):
        med.append(float(input(f'Média do {i+1}° item: ')))
        dp.append(float(input(f'Desvio-padrão do {i+1}° item: ')))
        print()
        
    if any(n <= 0 for n in dp):
        print('O desvio-padrão precisa ser maior que 0!')
        
    else:
        med_total = sum(med)
        dp_total = np.sqrt(sum(np.array(dp)**2))
        
        print('Escolha dentre as seguintes funções:')
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
                prob = mais_quant (med_total, dp_total, k)
                print_med_e_dp (med_total, dp_total)
                print()
                print(f'A probabilidade de ser mais que {k} é {100*prob:.2f}%')
                
            elif func == 'B':
                prob = ate_quant (med_total, dp_total, k)
                print_med_e_dp (med_total, dp_total)
                print()
                print(f'A probabilidade de ser menos que {k} é {100*prob:.2f}%')
        else:
            k1 = float(input('Coloque o limite inferior: '))
            k2 = float(input('Coloque o limite superior: '))
            print()
            
            if k1 > k2:
                print('O limite inferior não pode ser maior que o limite superior!')
            else:
                prob = entre (med_total, dp_total, k1, k2)
                print_med_e_dp (med_total, dp_total)
                print()
                print(f'A probabilidade de estar entre {k1} e {k2} é {100*prob:.2f}%')