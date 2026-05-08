def dechiffrer_viginere(key,msg):
    alpha ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = key.upper()
    key = [alpha.find(x) for x in key]
    msg= msg.upper().replace(" ","")
    out=''
    #print(key)
    for i,c in  enumerate(msg):
        #print(i%len(key))
        out+=chr((alpha.find(c)-key[i%len(key)])%26+ord('A'))
    return out

key="ESSATTC"

msg="PWUHB YHVWV EOBII FJEXL VYFKY LMOIV WCABH JJWMX GVTSJ SNUUX ALUMB QRHGL RTNTZ SBMBS YWEAB LWRWE MXEGX LJEWN OIKKA ZXEPS ARIXW XKMIO TPXKS PHLKX AGNWT PWUWL NBEML JEKXO TDSCX ICVVW SEXVX JWSWB HJJWN MXUGG FTKTK VWEEG MWRKQ SMFGH WUHBY HVWEE GMOSF GAEIJ ETLIJ NGGGE MXEGG ZAFYK GHWUS TKSYA DUMBN MKWCX IGRVS NMVQQ EWCHF RSKSN MVGXL WMMAQ HWJSB LVISA NLBNE FSLRL GHWXR JNGRU WSVXS YAWSM NPENS NMTII VUILB HWMJL XLELA XFKXO IFLSF HPSSD PATDX AIUXL"

print(dechiffrer_viginere(key,msg))