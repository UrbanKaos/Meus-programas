A = float(input("Digite o primeiro número: "))
B = float(input("Digite o segundo número: "))
if A > B:
    print("O menor número é: %.1f" % B)
    print("O maior número é: %.1f" % A)
elif A == B:
    print("Os dois números são iguais")
else:
    print("O menor número é: %.1f" % A)
    print("O maior número é: %.1f" % B)
