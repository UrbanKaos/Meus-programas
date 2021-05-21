Q = int(input("Digite a quantidade de números reais que este programa vai ler: "))
somax = 0
soman = 0
Cont = 0
while Cont <= Q:
    if Cont == 0:
        N = int(input("Digite um número inteiro: "))
        soman = soman + N
    elif Cont > 0:
        X = float(input("Digite um número real: "))
        somax = somax + X
    Cont = Cont + 1
soma = soman + somax
print("A Soma de tudo é: ", soma)

