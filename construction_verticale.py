import math
import numpy as np

#with numpy in two lines
def construction_verticale1(mot):
    key=list(mot.upper().replace(' ',''))
    #l=key+[chr(ord('A')+i) for i in range(math.ceil(26/len(key))*len(key)) if chr(ord('A')+i) not in key]
    return "".join(x for x in np.array(key+[chr(ord('A')+i) for i in range(math.ceil(26/len(key))*len(key)) if chr(ord('A')+i) not in key]).reshape(-1,len(key)).T.reshape(1,-1).flatten().tolist() if x.isalpha())

#teacher's method
def construction_verticale2(mot):
    key=list(mot.upper().replace(' ',''))
    nc=len(key)#columns
    nl=math.ceil(26/nc)#rows
    l=key
    for i in range(26):
        ch= chr(i+ord('A'))
        if ch not in key:
            l.append(ch)
    out=""
    for i in range(nc):
        for j in range(nl):
            if j*nc+i <26:
                out+=l[j*nc+i]
    return out

#with O(n) complexity
def construction_verticale3(mot):
    key=list(mot.upper().replace(' ',''))
    nc=len(key)
    nl=math.ceil(26/nc)
    l=key+[chr(ord('A')+i) for i in range(nc*nl) if chr(ord('A')+i) not in key]
    return "".join([l[(i%nl)*nc+( i // nl)] for i in range(nc*nl) if (i%nl)*nc+( i // nl) <26])

def chiffrer(mot, msg, isChiffrement= False):
    cat=construction_verticale3(mot)
    print(cat)
    out=[]
    if isChiffrement:
        for i in msg:
            if i == ' ':
                out.append(i)
            else:
                out.append(cat[ord(i)-ord('A')])
    else:
        for i in msg:
            if i == ' ':
                out.append(i)
            else:
                out.append(chr(cat.index(i)+ord('A')))
    return "".join(out)

#print(construction_verticale3('CYBER'))
code=chiffrer('CYBER','MERCI', True)
#print(code)
code_dechiffre=chiffrer('CYBER',code, False)
#print(code_dechiffre)


"""
================================================================================
def unique(mot):
    l= list(mot)
    i=0
    while i < len(l):
        if l.index(l[i])!= i or l[i]==' ':
            l.pop(i)
        i+=1
    return l
#My first try 
def construction_verticale(l):
    nc=len(l)
    nl=math.ceil(26/len(l))
    m=[]
    m.append(l) 
    c=0
    for i in range(1,nl):
        j=0
        line=[]
        while j < nc and c<26:
            let=chr(c+ord('A'))
            if let in l:
                c+=1
            else:
                line.append(let)
                c+=1
                j+=1
        m.append(line)
    cat={}
    for i in range(nc):
        for j in range(nl):
            if j==nl-1 and i>=len(m[nl-1]):
                continue
            cat[chr(i+j+ord('A'))]=m[j][i]
    return cat
"""