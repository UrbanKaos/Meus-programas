lista = []
acum = -1
X = int(input("Digite um número: "))
while X != 0 and X > 0:
    lista.append(X)
    acum = acum + 1
    X = int(input("Digite um número: "))
ind = 0
while acum >= 0:
    print(lista[acum])
    acum = acum - 1
    

    
