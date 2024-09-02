if __name__ == '__main__':
    seq = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        seq.append([name, score])
        
    scores = dict(seq).values()
    minim = min(scores)
    minim2 = max(scores)
    indexes = []
    for ind, s in enumerate(seq):
        if minim2 > s[1] > minim:
            indexes = [ind]
            minim2 = s[1]
        elif s[1]==minim2:
            indexes.append(ind)
            
    s = []
    for i in indexes:
        s.append(seq[i])
    s.sort()
    for e in s:
        print(e[0])
