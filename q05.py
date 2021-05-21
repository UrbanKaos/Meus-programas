cont = 1
vp = 0
vi = 0
vpo = 0
vn = 0
while cont <= 5:
    cont = cont + 1
    X = int(input())
    if X % 2 == 0:
        vp = vp + 1
    if X % 2 == 1:
        vi = vi + 1
    if X > 0:
        vpo = vpo + 1
    if X < 0:
        vn = vn + 1
print("{} valor(es) par(es)".format(vp))
print("{} valor(es) impar(es)".format(vi))
print("{} valor(es) positivo(s)".format(vpo))
print("{} valor(es) negativo(s)".format(vn))
