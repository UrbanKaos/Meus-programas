cont = 0
inv = []
i = 0
A = []
LMin = int(input("Digite o valor minimo: "))
LMax = int(input("Digite o valor máximo: "))
if LMin > LMax:
    inv.append(LMin)
    inv.append(LMax)
    inv.sort()
    LMin = inv[(0)]
    LMax = inv[(1)]
if LMin < LMax:
    while cont < 10:
        X = int(input("Digite um valor dentro do intervalo: "))
        if X >= LMin and X <= LMax:
            A.append(X)
            i = i + 1
        cont = cont + 1
print("Foram digitados", i, "números dentro do intervalo. Eles são: ", A)

    
