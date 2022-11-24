x = input().split()
A = (x[0])
B = (x[1])
C = (x[2])

x1 = input().split()
X = (x1[0])
Y = (x1[1])
Z = (x1[2])


P = int(X / A)
P01 = int(Y / B)
P02 = int(Z / C)

RESUL =int (P * P01 * P02)
print(P)
print(P01)
print(P02)
print(RESUL)

