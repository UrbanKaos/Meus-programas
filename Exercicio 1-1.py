P = int(input("Digite o primeiro termo: "))
R = int(input("Digite a razão: "))
N = int(input("Digite a quantidade de elementos: "))
Cont = 1
soma = 0
while Cont <= N:
    print("Termo", Cont, "da PG =", P)
    soma = soma + P
    P = P * R
    Cont = Cont + 1
print("A Soma de todos os termos é: ", soma)

