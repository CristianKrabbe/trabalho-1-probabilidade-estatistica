import math

med = float(input('Taxa média no intervalo de tempo: '))
temp_med = float(input('Intervalo de tempo da média (em minutos): '))
k = int(input('Quantidade desejada no intervalo de tempo: '))
temp_des = float(input('Intervalo de tempo desejado (em minutos): '))


if k < 0 or med < 0:
    print('Nem a média e nem as ocorrências podem ser negativas!')
elif temp_med <= 0 or temp_des < 0:
    print('Tempo médio não pode ser 0 e nenhum tempo pode ser negativo!')
   
else:
    lamb = med * (temp_des/temp_med)
    prob = (math.exp(-lamb)*(lamb**k))/math.factorial(k)

    print()
    print(f'A probabilidade de {k} acontecer em {temp_des} minuto(s) é {100*prob:.2f}%')