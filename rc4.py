def ksa(key):
    s = []
    for i in range(0, 256):
        s.append(i)
    j = 0
    for i in range(0, 256):
        j = (j+s[i]+key[i%len(key)])%256
        hlp = s[i]
        s[i] = s[j]
        s[j] = hlp
    return s

def prga(s):
    i = 0
    j = 0
    c = s.copy()
    for l in range(0, len(s)):
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        hlp = s[i]
        s[i] = s[j]
        s[j] = hlp
        k = (s[i] + s[j]) % 256
        c[i] = s[k]
    return c

def xor_with_keystream(data, keystream):
    return [data[i] ^ keystream[i] for i in range(len(data))]


def getKeyStream():
    key = "This Is a Secret Key"
    k = []
    for i in range(0, len(key)):
        k.append(ord(key[i]))
    s = ksa(k)
    keystream = prga(s)
    return keystream


def encryptData(plain_text):
    keystream = getKeyStream()
    data = []
    for i in plain_text:
        data.append(ord(i))
    encrypted_message = xor_with_keystream(data,keystream)
    encrypted_text = ""
    for i in encrypted_message:
        encrypted_text = encrypted_text+chr(i)
    return encrypted_text


def decryptData(plain_text):
    keystream = getKeyStream()
    data = []
    for i in plain_text:
        data.append(ord(i))
    encrypted_message = xor_with_keystream(data,keystream)
    encrypted_text = ""
    for i in encrypted_message:
        encrypted_text = encrypted_text+chr(i)
    return encrypted_text
