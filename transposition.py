import math 
def transposition(key):
    alpha ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    keyList = sorted(list(key.upper()))
    print(keyList)
    orderList=[]
    done=[]
    for c in key :        
        n=keyList.index(c)
        if(c in done ):
            i=n
            j=1
            while  i+j<len(key) and keyList[i+j]==keyList[i]:
                j+=1
                n+=1
        done.append(c)
        orderList.append(n)
    return orderList

def dechiffrer(key,msg):
    msg= msg.upper().replace(" ","")
    orderList =  transposition(key)
    print(orderList)
    l=len(orderList)
    n= math.ceil(len(msg)/l)
    out=[]
    for i in range(n): 
        portion = [ ]
        for j in range(l):
            k= i*len(orderList)+j
            if k<len(msg):
                portion.append(msg[k])
            else:
                portion.append('X')
        #print(portion) 
        portionD=[]   
        for j in range(l):
            #print(portion[orderList[j]])
            portionD.append(portion[orderList.index(j)])
        #print(portionD)
        out=out+portionD
    return "".join(out)

msg = 'EENFE FCMLR HISSS SAORA PTNRT PTDIM FEOII ONNIN REAUL PQEFA STCTS EELDR NTESE UAPCR EEIDL XTTIL UEESQ LUUUE SONUH ECDGR ARERE DFSSY NENEA LAEDL ESCUE RSENQ TTTUX DREEN ESTCE EEMRI REPFF HDPER RENET ECDOL TNSOI TIRAI LURUH ECLBN PDABO FPTNR ERAIT EMFAI MINSS ORTPO NIEAR PENTA MEPSE ECEET SDSDU INYEE ETCTX RTERP'   
key='CRYPTOGRAPHIE'

#print(dechiffrer(key,msg))    


    