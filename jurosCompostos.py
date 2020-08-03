import math
print('=-'* 15, 'JUROS COMPOSTOS', '=-'*15)
print('Opções:')
print('[1]VALOR FUTURO\n[2]VALOR PRESENTE\n[3]TAXA DE JUROS\n[4]NÚMERO DE PERÍODOS')
escolha = int(input('QUAL CÁLCULO DESEJA FAZER? '))
print('=-'* 38)
while True:
    if escolha != 1 and escolha !=2 and escolha != 3 and escolha != 4:
        print('Comando inválido, tente novamente')
        escolha = int(input('QUAL CÁLCULO DESEJA FAZER? '))
    else:
        break
if escolha == 1:
    print('CALCULAR O VALOR FUTURO:  F = P * (1 + i)^n') #o i/100 é porque na coleta de dados o usuário coloca a taxa em porcentagem
    p = float(input('Valor presente(P): '))
    i = float(input('Taxa de juros em porcentagem(i): '))
    n = float(input('Número de períodos(n): '))
    f = p * ((1+(i/100))**n)
    print (f'Valor futuro = {f}')
elif escolha == 2:
    print('CALCULAR O VALOR PRESENTE: P = F/(1 + i)^n')
    f = float(input('Valor futuro(F): '))
    i = float(input('Taxa de juros em porcentagem(i): '))
    n = float(input('Número de períodos(n): '))
    p = f/((1+(i/100))**n)
    print(f'O valor presente é {p} ')
elif escolha == 3:
    print('CALCULAR A TAXA DE JUROS: i = ((F/P)^1/n) - 1')
    f = float(input('Valor futuro(F): '))
    p = float(input('Valor presente(P): '))
    n = float(input('Número de períodos(n): '))
    div = f/p
    pot = 1/n
    potdiv = div**pot
    i = (potdiv - 1)*100
    print(f'Taxa de juros = {i}%')
elif escolha == 4:
    print('CALCULA NÚMERO DE PERÍODOS: n = log(F/P)/log(1+i) ')
    print('Dados')
    p = float(input('Valor presente(P): '))
    i = float(input('Taxa de juros em porcentagem(i): '))
    f = float(input('Valor futuro(F): '))
    fp = f/p
    i1 = 1+(i/100)
    logfp = math.log(fp)
    logi1 = math.log(i1)
    n = logfp/logi1
    print(f'Número de períodos = {n}')

