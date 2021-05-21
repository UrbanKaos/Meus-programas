cont = 0
lista = []
lista2 = []
while cont < 20:
    if cont < 10:
        X = int(input("Digite um número para a primeira lista: "))
        lista.append(X)
    if cont >= 10:
        Y = int(input("Digite um número para a segunda lista: "))
        lista2.append(Y)
    cont = cont + 1
soma = lista + lista2
print("As duas listas são: ", soma)
        
