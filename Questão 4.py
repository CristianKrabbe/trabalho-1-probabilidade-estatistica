pop = int(input('Tamanho da população: '))
amostra = int(input('Tamanho da amostra a ser considerada: '))

prob = 1

if pop < 1:
    print('A população total precisa ser 1 ou mais!')

elif pop < amostra:
    print('A população total precisa ser maior que a amostra escolhida e maior!')

else:
    
    n = int(input('Amostras a serem tiradas sem reposição: '))
    
    for i in range (n):
        prob = prob*(amostra/pop)
        amostra = amostra - 1
        pop = pop - 1
    
    print()
    print(f'Tem {100*prob:.2f}% de chance de selecionar alguém da amostra escolhida')