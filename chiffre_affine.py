def chiffre_affine(a,b):

    dic={}
    for i in range(26):
        x=i
        y=(a*x+b)%26
        dic[chr(x+ord('A'))]= chr(y+ord('A'))
    return dic
def dechiffrer_affine(a,b):
    dic={}
    a1=1
    while ((a*a1)%26) != 1:
            #print(a1,' ',((a*a1)%26))
            a1+=2
    #print(a1,' ',((a*a1)%26))
    for i in range(26):
        y=i
        x=a1*(y-b)%26        
        dic[chr(y+ord('A'))]=chr(x+ord('A'))
    return dic
        

def chiffrer(a,b,text,isChiffrer):
    if (isChiffrer):
        dic=chiffre_affine(a,b)
    else :
        dic=dechiffrer_affine(a,b)    
    print(dic)
    text=text.upper()
    out=[]
    for char in text :
        if ord(char)-ord('A') in range(26):
            out.append(dic[char])
        else :
            out.append(char)    
    return "".join(out)


text="deux entiers a et b sont choisis comme clef chaque lettre claire est dabord remplace par son equivalent numerique x puis chiffree par le calcul du reste de la division euclidienne par vingt-six"
code="qlpai ndchs sanaw nbnff txnhw "
#print(chiffrer(7,16,text,True))
print(chiffrer(5,19,code.replace(' ',''),False))
#hlgvp htpgn gkhna edlbq ahfng kanon alnku hgxkd hgvtf fldhn wnanf knint eqwpf yitgf wtihu hfhlg qtauh gxkfh e