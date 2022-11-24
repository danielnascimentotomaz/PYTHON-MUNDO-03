x = input().split()
A = int(x[0])
B = int(x[1])
C = int(x[2])

x1 = input().split()
X = int(x1[0])
Y = int(x1[1])
Z = int(x1[2])


P = int(X / A)
P01 = int(Y / B)
P02 = int(Z / C)

RESUL =int (P * P01 * P02)
print(RESUL)






