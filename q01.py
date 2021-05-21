print("Marcos Vinicius Andrade Urban\n")

X = int(input("Digite um número: "))
H = X // 3600
M = (X % 3600) // 60 
S = (X % 3600) % 60

print("\nEm {} seguntos, tem:".format(X))
print("\n{:.0f} horas, {:.0f} minutos, {:.0f} segundos".format(H, M, S))
