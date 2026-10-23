
A = float(input('Limite inicial (A): '))
B = float(input('Limite final (B): '))

if A >= B:
    print('O limite inicial não pode ser maior ou igual que o limite final!')

else:
    print()
    print(f'Considerando o limite inicial e final ({A} e {B}), escolha os limites para o cálculo da probabilidade:')
    C = float(input('Limite inicial desejado (C): '))
    D = float(input('Limite final desejado (D): '))
    
    if C > D:
        print('O limite inicial desejado não pode ser maior que o limite final desejado!')

    elif C > B or D < A:
        print(f'Está totalmente fora dos limites A e B ({A} e {B})!')
    else:
        if C < A:
            C = A
       
        if D > B:
            D = B
    
        med = (B + A) / 2
        variancia = ((B - A)**2) / 12   
        prob = (D - C) / (B - A)
        
        print()
        print(f'A média é {med:.2f} e a variância é {variancia:.2f}')
        print()
        print(f'A probabilidade de {C} < X < {D} (dentro de {A} e {B}) é {100*prob:.2f}%')