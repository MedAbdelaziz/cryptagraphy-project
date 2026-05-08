
def dechiffrer(key,msg):
    alpha ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    msg= msg.upper().replace(" ","")
    l=len(key)
    out=''
    j=0
    for i in msg:
        if(j%l==0):
            j=0
        decalage=alpha.find(key[j])//2
        second=alpha[13:]
        alpha1 = alpha[:13]+second[-decalage:]+second[:-decalage]  
        out+=alpha1[(alpha1.find(i)+13)%26]
        j+=1
    return out

msg="SRMYT EPFOG CBYAH"
key='NAPLES'

#print(dechiffrer(key,msg))  


    