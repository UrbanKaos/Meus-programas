print("Marcos Vinicius Andrade Urban\n")


LMin = int(input("Digite o valor mínimo: "))
LMax = int(input("Digite o valor máximo: "))
if LMin <= 0:
    while LMin <= 0:
        print("\nValor mínimo inválido, digite novamente\n")
        LMin = int(input("Digite o valor mínimo: "))

if LMax < LMin:
    while LMin > LMax:
        print("\nValor máximo inválido, digite novamente\n")
        LMax = int(input("Digite o valor mínimo: "))

X = int(input("Digite X: "))
if X == 0:
    while X == 0:
        print("\nValor de X inválido, digite novamente\n")
        X = int(input("Digite o valor de X: "))

A = int(input("Digite um número inteiro para a lista: "))
L = []
cont = 0
Soma = 0
if A == 0:
    while A == 0:
        print("\nValor igual a 0, somente utilize 0 para sair, digite novamente\n")
        A = int(input("Digite um número inteiro para a lista: "))
  
while A != 0:
    if A >= LMin and A <= LMax and A % X == 0:
        if A in L:
            pass
        else:
            L.append(A)
            cont = cont + 1
            Soma = Soma + A
            Media = Soma / cont
    A = int(input("Digite um número inteiro para a lista: "))

print("\nRESULTADOS\n")
print("A lista completa é: ", L)
print("\nA quantidade de elementos da lista é: ", cont)
print("\nA soma de todos os valores é: ", Soma)
print("\nA média dos valores é: ", Media)

    


