import math
from multiprocessing import Process

def inverse_mod_n(n,b):
    n0=n
    b0=b
    t0=0
    t=1
    q = math.floor(n0/b0)
    r = n0 - q * b0
    while(r>0):
        time= t0 - q*t
        if time>0:
            time= time%n 
        else:
            time= n- ((-time)%n) 
        t0 = t 
        t = time 
        n0 = b0
        b0 = r
        q = math.floor(n0/b0)
        r = n0 - q * b0
    if b0 != 1 :
        print ("pas d'inverse")
    else :
        print (t)

rsa(2668,335)

def prepare(msg):
    alpha= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha = alpha + alpha.lower()
    alphnum=''
    for c in msg:
        alphnum += alpha.find(c)
def isPremier(n):
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if n%i ==0:
            return False
    return True
def generatePremier(min , max):
    l=[]
    for i in range(min,max+1):
        if isPremier(i):
            l.append(i)
    return l


def generate_cle_rsa(p,q,e):
    n=p*q
    fi_n =(p-1)*(q-1)
    d=inverse_mod_n(e,fi_n)
    return {"public":(e,fi_n),"private":(d,fi_n)}

if __name__ == "__main__":
    p = Process(target=generatePremier(1000000,10000000))
    p.start()
    p.join()
#message = 30 32 30 36 27 32 46 47 27 48 41 27 28 39 34 42 45 36 47 35 40  32 