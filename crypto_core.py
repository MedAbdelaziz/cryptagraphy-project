import math

# ----------------- AFFINE -----------------
def chiffre_affine(a, b, text, is_encrypt=True):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return "Error: a and b must be integers."
        
    if not is_encrypt:
        a_inv = 1
        while ((a * a_inv) % 26) != 1:
            if a_inv > 100: 
                return "Error: 'a' must be coprime with 26."
            a_inv += 2
        a = a_inv
        b = -b * a_inv

    dic = {}
    for i in range(26):
        y = (a * i + b) % 26
        dic[chr(i + ord('A'))] = chr(y + ord('A'))
    
    text = text.upper()
    out = []
    for char in text:
        if 'A' <= char <= 'Z':
            out.append(dic[char])
        else:
            out.append(char)
    return "".join(out)

# ----------------- VIGENERE -----------------
def vigenere(key, text, is_encrypt=True):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = key.upper()
    key_nums = [alpha.find(x) for x in key if x in alpha]
    if not key_nums: return text

    text = text.upper()
    out = ''
    j = 0
    for c in text:
        if c in alpha:
            shift = key_nums[j % len(key_nums)]
            if not is_encrypt:
                shift = -shift
            out += chr((alpha.find(c) + shift) % 26 + ord('A'))
            j += 1
        else:
             out += c
    return out

# ----------------- PORTA -----------------
def porta(key, text, is_encrypt=True):
    # Porta is reciprocal, encryption == decryption
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = text.upper()
    key = "".join([c.upper() for c in key if c.upper() in alpha])
    out = ''
    j = 0
    l = len(key)
    if l == 0: return text
    
    for i in text:
        if i in alpha:
            decalage = alpha.find(key[j % l]) // 2
            second = alpha[13:]
            alpha1 = alpha[:13] + second[-decalage:] + second[:-decalage]
            out += alpha1[(alpha1.find(i) + 13) % 26]
            j += 1
        else:
            out += i
    return out

# ----------------- TRANSPOSITION -----------------
def get_transposition_order(key):
    # Strip spaces for exact key ordering logic
    key = key.upper().replace(' ', '')
    keyList = sorted(list(key))
    orderList = []
    done = []
    for c in key:
        n = keyList.index(c)
        if c in done:
            i = n
            j = 1
            while i + j < len(key) and keyList[i + j] == keyList[i]:
                j += 1
                n += 1
        done.append(c)
        orderList.append(n)
    return orderList

def transposition(key, text, is_encrypt=True):
    text_clean = text.upper().replace(" ", "")
    # Remove non-alphabet for standard transposition, but keep original logic
    if not key: return text
    orderList = get_transposition_order(key)
    l = len(orderList)
    if l == 0: return text
    
    n_rows = math.ceil(len(text_clean) / l)
    
    if is_encrypt:
        text_padded = text_clean + 'X' * (n_rows * l - len(text_clean))
        out = ""
        for i in range(l):
            col_idx = orderList.index(i)
            # read vertically column by column
            for r in range(n_rows):
                out += text_padded[r * l + col_idx]
        return out
    else:
        out = []
        for i in range(n_rows):
            portion = []
            for j in range(l):
                k = i * l + j # Wait, decryption reading blocks is different in original code?
                # Original decrypter generated blocks, let's keep original format logic
                if k < len(text_clean):
                    portion.append(text_clean[k])
                else:
                    portion.append('X')
            portionD = []
            for j in range(l):
                 if orderList.index(j) < len(portion):
                     portionD.append(portion[orderList.index(j)])
                 else:
                     portionD.append('X')
            out = out + portionD
        return "".join(out).rstrip('X')

# ----------------- CONSTRUCTION VERTICALE -----------------
def construction_verticale_grid(key):
    key_list = list(key.upper().replace(' ',''))
    seen = []
    key_dedup = []
    for char in key_list:
        if char not in seen and char.isalpha():
            seen.append(char)
            key_dedup.append(char)
            
    nc = len(key_dedup)
    if nc == 0: return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    nl = math.ceil(26 / nc)
    l = key_dedup + [chr(ord('A')+i) for i in range(nc * nl) if chr(ord('A')+i) not in key_dedup]
    cat = "".join([l[(i % nl) * nc + (i // nl)] for i in range(nc * nl) if (i % nl) * nc + (i // nl) < 26])
    return cat

def chiffrer_verticale(key, text, is_encrypt=True):
    cat = construction_verticale_grid(key)
    out = []
    text = text.upper()
    if is_encrypt:
        for i in text:
            if 'A' <= i <= 'Z':
                out.append(cat[ord(i) - ord('A')])
            else:
                out.append(i)
    else:
        for i in text:
            if i in cat:
                out.append(chr(cat.index(i) + ord('A')))
            else:
                out.append(i)
    return "".join(out)

# ----------------- ADFGVX -----------------
def get_adfgvx_grid():
    return [
        ['C', '1', '0', 'F', 'W', 'J'],
        ['Y', 'M', 'T', '5', 'B', '4'],
        ['I', '7', 'A', '2', '8', 'S'],
        ['P', '3', 'O', 'Q', 'H', 'X'],
        ['K', 'E', 'U', 'L', '6', 'D'],
        ['V', 'R', 'G', 'Z', 'N', '9']
    ]

def get_adfgvx_dict():
    grid = get_adfgvx_grid()
    a = 'ADFGVX' # changed to ADFGVX explicitly to cover 6x6
    alphaDic = {}
    for r in range(6):
        for c in range(6):
            alphaDic[grid[r][c]] = a[r] + a[c]
    return alphaDic

def get_adfgvx_reverse_dict():
    grid = get_adfgvx_grid()
    a = 'ADFGVX'
    revDic = {}
    for r in range(6):
        for c in range(6):
            revDic[a[r] + a[c]] = grid[r][c]
    return revDic
    
def adfgvx(key, text, is_encrypt=True):
    text = text.upper().replace(" ", "")
    key = key.upper()
    if not key: return text
    
    if is_encrypt:
        alphaDic = get_adfgvx_dict()
        subbed = ""
        for char in text:
            if char in alphaDic:
                subbed += alphaDic[char]
            else:
                # pad or skip unknown characters
                pass
        return transposition(key, subbed, is_encrypt=True)
    else:
        untransposed = transposition(key, text, is_encrypt=False)
        revDic = get_adfgvx_reverse_dict()
        out = ""
        for i in range(0, len(untransposed)-1, 2):
            pair = untransposed[i:i+2]
            if pair in revDic:
                out += revDic[pair]
        return out

# ----------------- FREQUENCY ANALYSIS -----------------
def ic(l):
    ic_val = 0
    n = sum(l)
    if n <= 1: return 0
    for i in l:
        ic_val += i * (i - 1)
    return ic_val / (n * (n - 1))

def lenKey(msg):
    msg = "".join([c for c in msg.upper() if c.isalpha()])
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    icN = 0
    delta = 1
    while icN < 0.05 and delta < 20: 
        if delta >= len(msg): break
        echantillion = [msg[i] for i in range(0, len(msg), delta)]
        freq = [echantillion.count(c) for c in alpha]
        icN = ic(freq)
        delta += 1
    longueur = delta - 1 if delta > 1 else 1
    return icN, longueur

def findKey(msg):
    msg = "".join([c for c in msg.upper() if c.isalpha()])
    if not msg: return "", 0, 0
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    icN, delta = lenKey(msg)
    
    if delta == 0: return "", 0, 0
    
    texts = [''] * delta
    for i in range(len(msg)):
        texts[i % delta] += msg[i]
        
    cle = ''
    for text in texts:
        freq = [text.count(c) for c in alpha]
        maxI = freq.index(max(freq)) if freq else 0
        decalage = maxI - 4  # 'E' is 4th index (0-based)
        cle += alpha[decalage % 26]
    return cle, delta, icN
