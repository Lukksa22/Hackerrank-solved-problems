def merge_the_tools(string, k):
    subs = []
    for i in range(0, len(string), k):
        sub = []
        for e in string[i:i+k]:
            if e not in sub:
                sub.append(e)
        print(''.join(sub))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)