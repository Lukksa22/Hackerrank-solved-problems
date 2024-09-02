def func(arr):
    maxim = max(arr)
    second = min(arr)
    
    for e in arr:
        if second < e < maxim:
            second = e
            
    print(second)

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    func(arr)