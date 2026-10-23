import numpy as np

quant = int(input('Quantidade de itens a ser contabilizados (para variáveis idependentes): '))
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
        
    if any(n < 0 for n in dp):
        print('O desvio-padrão não pode ser negativo!')
        
    else:
        medtotal = sum(med)
        dptotal = np.sqrt(sum(np.array(dp)**2))
        
        print(f'A média total é {medtotal:.2f}')
        print(f'O desvio-padrão total é {dptotal:.2f}')