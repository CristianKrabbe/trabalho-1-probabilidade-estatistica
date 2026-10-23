pop = int(input('Tamanho da população: '))
casos = int(input('Tamanho da amostra a ser considerada: '))

if pop < 1:
    print('A população total precisa ser 1 ou mais!')

elif casos < 1: 
    print('A amostra selecionada precisa ser 1 ou mais!')

elif pop < casos:
    print('A população total precisa ser maior que a amostra escolhida e maior!')
    
else:
    prob = casos / pop
    
    print()
    print (f'A chance de fracasso é {100*(1 - prob):.2f}%')