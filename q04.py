cont = 0
inv = []
i = 0
f = 0
A = []
R = []
N = int(input("Digite a quantidade de valores que esse programa irá ler: "))
LMin = int(input("Digite o valor minimo: "))
LMax = int(input("Digite o valor máximo: "))
if LMin > LMax:
    print("Foi detectado que o valor minimo digitado foi maior que o valor maximo")
    print("Invertendo...")
    inv.append(LMin)
    inv.append(LMax)
    inv.sort()
    LMin = inv[(0)]
    LMax = inv[(1)]
if LMin < LMax:
    while cont < N:
        X = int(input("Digite um valor dentro do intervalo: "))
        if X >= LMin and X <= LMax:
            A.append(X)
            i = i + 1
        if X < LMin or X > LMax:
            R.append(X)
            f = f + 1
        cont = cont + 1
print("Foram digitados", i, "números dentro do intervalo. Eles são: ", A)

print("Foram digitados", f, "números fora do intervalo. Eles são: ", R)
    
