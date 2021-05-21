A = str(input("Insira seu nome: "))
B = float(input("Insira seu peso: "))
if B < 65:
    print("O lutador", A, "pesa", B, "kg e se enquadra na categoria Pena.")
elif B >= 65 and B < 72:
    print("O lutador %s" % A, "pesa %.1f" % B, "kg e se enquadra na categoria Leve.")
elif B >= 72 and B < 79:
    print("O lutador %s" % A, "pesa %.1f" % B, "kg e se enquadra na categoria Ligeiro.")
elif B >= 79 and B < 86:
    print("O lutador %s" % A, "pesa %.1f" % B, "kg e se enquadra na categoria Meio médio.")
elif B >= 86 and B < 93:
    print("O lutador %s" % A, "pesa %.1f" % B, "kg e se enquadra na categoria Médio.")
elif B >= 93 and B < 100:
    print("O lutador %s" % A, "pesa %.1f" % B, "kg e se enquadra na categoria Meio pesado.")
else:
    print("O lutador %s" % A, "pesa %.1f" % B, "kg e se enquadra na categoria Pesado.")
