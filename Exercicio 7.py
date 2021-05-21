A = float(input("Digite o valor do primeiro coeficiente: "))
B = float(input("Digite o valor do segundo coeficiente: "))
C = float(input("Digite o valor do terceiro coeficiente: "))
delta = B ** 2 - 4 * A * C
raizdelta = delta ** 0.5
x1 = (-B + raizdelta) / (2 * A)
x2 = (-B - raizdelta) / (2 * A)
x0 = -B / (2 * A)
if delta > 0:
    print("x1 = ", x1)
    print("x2 = ", x2)
elif delta == 0:
    print("x = ", x0)
else:
    print("Não há raizes reais")
