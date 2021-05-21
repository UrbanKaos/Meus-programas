X = float(input())
if X <= 400.00:
    r = (X * 15) / 100
    ns = r + X
    p = 15
if X > 400.00 and X <= 800.00:
    r = (X * 12) / 100
    ns = r + X
    p = 12
if X > 800.00 and X <= 1200.00:
     r = (X * 10) / 100
     ns = r + X
     p = 10
if X > 1200.00 and X <= 2000.00:
     r = (X * 7) / 100
     ns = r + X
     p = 7
if X > 2000.00:
     r = (X * 4) / 100
     ns = r + X
     p = 4
print("Novo salario: {:.2f}".format(ns))
print("Reajuste ganho: {:.2f}".format(r))
print("Em percentual: {} %".format(p))
