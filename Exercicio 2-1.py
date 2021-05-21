somap = 0
soman = 0
X = 1
while X != 0:
    X = int(input("Digite o X: "))
    if X > 0:
        somap = somap + X
    else:
        soman = soman + X
        
print("Total dos positivos =", somap)
print("Total dos negativos =", soman)
