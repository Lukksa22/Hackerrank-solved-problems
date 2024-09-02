def minion_game(string: str):
    players = {
        'Stuart':0,
        'Kevin':0
        }
    
    vowels = 'AEIOU'
    for i in range(len(string)):

        if string[i] in vowels:
            players["Kevin"] += len(string)-i
            
        else:
            players["Stuart"] += len(string)-i

    if players['Kevin']>players['Stuart']:
        result = 'Kevin ' + str(players['Kevin'])
    elif players['Kevin']<players['Stuart']:
        result = 'Stuart ' + str(players['Stuart'])
    else:
        result = 'Draw'

    print(result)

if __name__ == '__main__':
    s = input()
    minion_game(s)