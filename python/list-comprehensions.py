def func(x, y, z, n):
    seq = []
        
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                tupl = [i, j, k]
                if sum(tupl) != n:
                    seq.append(tupl)
    return seq
    
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(func(x, y, z, n))
