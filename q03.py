print("Marcos Vinicius Andrade Urban/n")



NV = int(input("Digite a quantidade de vendas no varejo: "))
if NV <= 0:
    while NV <= 0:
        print("ERRO, valor digitado menor ou igual a 0! Digite novamente")
        NV = int(input("Digite a quantidade de vendas no varejo: "))
cont = 0
vtv = 0
vta = 0
A = 0
while cont < NV:
    x = input("Digite o código e a quantidade de vendas: ").split()
    cod, qv, = x
    cont = cont + 1
    if cod == '16' and float(qv) < 50:
        A = A + float(qv)
        PUA16 = 14.35 * A
        vtv = vtv + PUA16
    if cod == '16' and float(qv) >= 50:
        A = A + int(qv)
        PUA16 = 12.93 * A
        vta = vta + PUA16
    if cod == '23' and float(qv) < 100:
        A = A + float(qv)
        PUV23 = 35.12 * A
        vtv = vtv + PUV23
    if cod == '23' and float(qv) >= 100:
        A = A + float(qv)
        PUA23 = 29.85 * A
        vta = vta + PUA23
    if cod == '27' and float(qv) < 70:
        A = A + float(qv)
        PUV27 = 19.35 * A
        vtv = vtv + PUV27
    if cod == '27' and float(qv) >= 70:
        A = A + float(qv)
        PUA27 = 16.76 * A
        vta = vta + PUA27
    if cod == '34' and float(qv) < 40:
        A = A + float(qv)
        PUV34 = 63.40 * A
        vtv = vtv + PUV34
    if cod == '34' and float(qv) >= 40:
        A = A + float(qv)
        PUA34 = 58.25 * A
        vta = vta + PUA34
    A = 0

print("\nResultados\n")
print("Total de Vendas do Grupo Varejo: R${:.2f}".format(vtv))
print("Total de Vendas do Grupo Atacado: R${:.2f}".format(vta))
print("Vendas totais: R${:.2f}".format(vtv + vta))
        

print("\n\nTHE END")        
        


