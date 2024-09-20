from math import *

def func(X, Y, n):
    
    mnX = sum(X)/len(X)
    a = [pow(e-mnX, 2) for e in X]
    stdX = sqrt(sum(a)/ len(a))
    
    
    mnY = sum(Y)/len(Y)
    b = [pow(e-mnY, 2) for e in Y]
    stdY = sqrt(sum(b)/ len(b))
    cov = (sum( [ (X[i]-mnX) * (Y[i]-mnY) for i in range(n)] )) / (n*stdX*stdY)
    print(f'{cov:.3f}')

if __name__ == '__main__':
    n = int(input().strip())
    X = list(map(float, input().rstrip().split()))
    Y = list(map(float, input().rstrip().split()))
    func(X, Y, n)