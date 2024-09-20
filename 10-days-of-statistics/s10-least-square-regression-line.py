from math import *

X = [95, 85, 80, 70, 60]
Y = [85, 95, 70, 65, 70]

n = len(X)
mnX = sum(X)/len(X)
a = [pow(e-mnX, 2) for e in X]
stdX = sqrt(sum(a)/ len(a))


mnY = sum(Y)/len(Y)
b = [pow(e-mnY, 2) for e in Y]
stdY = sqrt(sum(b)/ len(b))
cov = (sum([(X[i]-mnX) * (Y[i]-mnY) for i in range(n)] )) / (n*stdX*stdY)

b = cov * (stdY/stdX)
a = mnY - b*mnX

print(f'{(a + b*80):.3f}')
