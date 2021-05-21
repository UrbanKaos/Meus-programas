N = int(input("Digite um número entre 0 e 50: "))
A = []
cont = 0
NEG = []
POS = []
somp = 0
somn = 0
if N < 0 or N > 50:
    while N < 0 or N > 50:
        print("Número Inválido")
        N = int(input("Digite um número entre 0 e 50: "))
    if N >= 0 and N <= 50:
        while cont < N:
            X = float(input("Digite um número: "))
            A.append(X)
            cont = cont + 1
        for B in A:
            if B >= 0:
                POS.append(B)
                somp = somp + 1
            elif B < 0:
                NEG.append(B)
                somn = somn + 1
print("Os valores negativos são:", NEG)
print("Os valores positivos são:", POS)
print("A lista de positivos contém", somp, "números. E a lista negativa contém", somn, "números.")
            
    
