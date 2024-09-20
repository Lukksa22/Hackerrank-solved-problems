if __name__ == "__main__":
    n = int(input())
    entries = {}
    for e in range(n):
        inp = input().strip()
        if inp != "":
            entry = tuple(inp.split())
            entries[entry[0]] = entry[1]
    
    
    req = input().strip()
    while req!='':
        
        if req in entries:
            print(f'{req}={entries[req]}')
        else:
            print("Not found")
        try:
            req = input().strip()
        except EOFError:
            req = ''