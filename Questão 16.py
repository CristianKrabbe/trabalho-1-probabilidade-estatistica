import math

erro = float(input('Taxa de falha (0-1): '))
if erro <= 0:
    print('O erro não pode ser negativo!')

else:
    temp = []
    quant_temp = int(input('Quantas possibilidades de tempos de sobrevivência (em horas) calcular: '))
    if quant_temp < 1:
        print('Pelo menos 1 tempo para calcular!')
    else:
        for i in range (quant_temp):
            temp.append(float(input(f'{1+i}° tempo (horas): ')))
        
        if any (n < 0 for n in temp):
            print('O tempo não pode ser negativo!')       
        
        else:
            print()
            prob = []
            for i in range (quant_temp):    
                prob.append(math.exp(-erro*temp[i]))
                print(f'Tem {100*prob[i]:.2f}% de chance de sobreviver {temp[i]} hora(s)')