import math
grid = [
    ['C', '1', '0', 'F', 'W', 'J'],
    ['Y', 'M', 'T', '5', 'B', '4'],
    ['I', '7', 'A', '2', '8', 'S'],
    ['P', '3', 'O', 'Q', 'H', 'X'],
    ['K', 'E', 'U', 'L', '6', 'D'],
    ['V', 'R', 'G', 'Z', 'N', '9']
]

def alpha(grid):
    a='ADFGX'
    alpha ='ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
    alphaDic={}
    for c in a:
        for d in a:
            alphaDic[grid[a.find(c)][a.find(d)]]=''+c+d
    return alphaDic

def surChiffrement(key,alphaDic,text):
    text= text.upper().replace(" ","")
    key=key.upper()
    col=[[] for i in range(len(key))]
    for i in range (len(text)):
        col[i%len(key)].append(alphaDic[text[i]])
        if(i>=len(text)):
            col[i%len(key)].append('X')
    order = [key.find(x) for x in sorted(list(key))]
    output=""
    for i in range(len(key)):
        for c in col[order[i]]:
            output.append(c)
    return output

msg= 'rendez-vous à 15h28 sur la térrasse'

print(alpha(grid))
surChiffrement('MOHAMED',alpha(grid),msg)
