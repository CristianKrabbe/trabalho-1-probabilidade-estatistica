
pop = int(input('Tamanho da população: '))
qgrupos = int(input('Quantidade de grupos (div exata da população): '))

if qgrupos == 0:
    print('Quantidade de grupos inválida!')

elif pop < qgrupos:
    print('Quantidade de grupos maior que a população!')

elif pop % qgrupos != 0:
    print('A divisão não fica exata!')
  
else:
    x = input('Grupo escolhido: ')

    tgrupo = pop / qgrupos
    prob = 1 - tgrupo / pop

    print(f'A probabilidade de retirar alguém que não faz parte do grupo {x} é {prob*100:.2f}%')