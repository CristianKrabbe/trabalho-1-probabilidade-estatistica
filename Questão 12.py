import math

quant_pop = int(input('Quantidade de populações: '))
pop = []
for i in range (quant_pop):
    pop.append(int(input(f'População {i+1}: ')))
    
if any(n < 0 for n in pop):
    print('Nenhuma população pode ser negativa!') 
   
else:
    pop_tot = sum(pop)
    if pop_tot < 1:
        print('A população total deve ser pelo menos 1"')
    
    else:    
        sort = int(input('Quantidade de sorteios: '))       
        if sort < 1:
            print('Precisa-se pelo menos 1 sorteio!')
        elif sort > pop_tot:
            print('Não podem ter mais sorteios do que a população total!')
            
        else: 
            pop_des = int(input('População desejada para o cálculo: '))
                
            if pop_des < 1 or pop_des > quant_pop:
                print('Deve ser alguma das populações já colocadas (1 até quant de população)!')
                
            else:
                pop_sort = int(input('Quantidade de pessoas desejadas nos sorteios: '))
                if pop_sort < 0 or pop_sort > pop[pop_des-1] or pop_sort > sort:
                    print('Não pode ser negativo, nem maior que a sua população e nem maior que a quantidade de sorteios!!')
                   
                else:                               
                    prob = (math.comb(pop[pop_des-1], pop_sort)*(math.comb(pop_tot-pop[pop_des-1], (sort-pop_sort))))/math.comb(pop_tot, sort)
                    print()
                    print(f'A probabilidade de sortear {pop_sort} pessoa(s) da população {pop_des} é {100*prob:.2f}%')