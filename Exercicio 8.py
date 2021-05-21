A = float(input("Digite o primeiro valor: "))
B = float(input("Digite o segundo valor: "))
C = float(input("Digite o terceiro valor: "))
if A < B + C and B < A + C and C < A + B:
    print("Sim, é um triangulo!")
    if A == B == C:
        print("Este triangulo é um triangulo equilátero")
    elif A != B != C != A:
        print("Este triangulo é um triangulo escaleno")
    else:
        print("Este triangulo é um triangulo isóceles")
else:
    print("Não é um triangulo!")



    

