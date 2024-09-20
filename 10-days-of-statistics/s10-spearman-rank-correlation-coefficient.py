from math import *

def func(X, Y, n):
    Xa = sorted(X)
    rankX = list(map(lambda x: Xa.index(x)+1, X))
    
    Ya = sorted(Y)
    rankY = list(map(lambda x: Ya.index(x)+1, Y))
    
    sumdsquare = sum([(rankY[i] - rankX[i])**2 for i in range(n)])
    
    rs = 1 - ((6*sumdsquare) / (n*((n**2) - 1)))
    
    print(f'{rs:.3f}')

if __name__ == '__main__':
    n = int(input().strip())
    X = list(map(float, input().rstrip().split()))
    Y = list(map(float, input().rstrip().split()))
    func(X, Y, n)