def ic(l):
    list=l
    ic=0
    n=sum(list)
    #print('       ')
    #print(n)
    for i in list:
        ic+=i*(i-1)
    return (ic/(n*n-1))

def lenKey(msg):
    msg= msg.upper().replace(" ","")
    alpha ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    icN=0
    delta=1
    while(icN <0.05 ):        
        echantillion=[msg[i] for i in range(0,len(msg),delta)]
        freq=[0]*26
        for i in alpha:
            freq.append(echantillion.count(i))
        icN=ic(freq)
        #print(echantillion)
        #print(freq)
        #print('delta: ',delta)
        #print('ic: ',icN)
        delta+=1
    print('longuer de cle: ',delta-1)
    print('ic: ',icN)
    return icN, delta-1

def findKey(msg):
    msg= msg.upper().replace(" ","")
    alpha ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    icN, delta= lenKey(msg)
    texts=['']*delta
    for i in range(len(msg)):
        texts[i%delta]+=msg[i]
    cle=''
    for text in texts:

        freq=[]
        for c in alpha:
            freq.append(text.count(c))
        maxI=freq.index(max(freq))
        decalage=maxI-4
        cle+=alpha[(decalage)%26]
    return cle


msg="ADLNE XDOYL SFYQQ BZEYF OQRLL AKLOW LLESS QBZOG VFQDL RYIWF OUTPI GQDSO KIUPS ZIZJU MGARG " \
"GWGFL SPIFX CBDOS PBIAI ZKLZT YAEXU GQAUD IHZHH NFUXQ GLRHM FQZHT QGKZC SOSMH BCZSQ HHGBL ADGKU " \
"HLCFY UQAVD GPDUF LCAQS AGLEP ISXIZ IQYUE DYOVI WEQVR DIOQG UOHEV IWMTS PDZQL EFGTG WWEDQ HFHLN " \
"FHHOC UTDSO QFSEE HLRTL RQRWQ GYEEW RGFJE EHHEA HCTMQ QGCID XXQZS EEXHX ZLSCY HXOWU UWVMB JEPIF " \
"MZJUX PHEHV CWEJQ CBEZG RDSSE DIVQO BLQTU AXLTQ WWBCY TQTDD ZHFAR GMHPO ZSSQB ZTMGN GBLOD KDZWZ " \
"AFMRZ BVNOS PYSYC UEOQE BIMTR GFIUF HHBFV MAYYA WYLQT UAXLT ATHZG AAOOD UBZIC YHPSW RAXHS SYEFH " \
"DURLR XIVPS CEXSS BSBRE IWFCB TQPDO CTMGR DGHLO BIQEH HCWHH ZCTBD IXESZ EZXUQ DYIEI VABAR QNRUB " \
"ALMJR ZRHTU SQADL NEXDO YWADQ LOSSL QWFUC URQXU AICEO EQABP CMPUQ ROAFW XESLN AZDZQ LAFXF UGJOP " \
"IOXVW INQBM VVOAV DOZLO DEQSS JLAYG IOATQ QFHAD ADILZ HLLOI VFIUL AKLOW LLXME DSKIE XUUPB EEIOA " \
"BSEEX HDALS PIOMZ PCQRF QOWAO LH"


list=[53,57,38,8,3,0,2,0,47,6,45,26,126,7,9,7,40,4,6,45,18,49,60,28,5,53]
#ic(list)
list2=[40,27,23,37,44,30,29,40,36,8,8,44,18,9,39,20,49,25,40,22,32,17,25,26,21,33]
#ic(list2)
#if ic<0.5 this is almost certainly not a language

print(findKey(msg))