from constants import defaultAllowedCharacter
from utils.main import getLength

# uses affine cipher
# seed :
# a = 9
# b = 3

# nilai default
allowedCharacters = defaultAllowedCharacter

aDefault = 9
bDefault = 3
mDefault = getLength(allowedCharacters) # how many characters allowed are


# modular multiplicative inverse a^-1 is
# 1 = a*a^-1 mod m
def getMMI(x, m = mDefault):
    xInverse = 0
    while (xInverse * x % m != 1):
        xInverse += 1
    
    return xInverse

# affine cipher
def getEncryptSeed(x, a = aDefault, b = bDefault, m = mDefault):
    return (a*x + b) % m

def getDecryptSeed(x, a=aDefault, b = bDefault, m = mDefault):
    return getMMI(a) * (x - b) % m

# fungsi handle untuk list value
def encryptList(li):
    for i in range(len(li)):
        li[i] = getEncryptSeed(li[i])
    return li

def decryptList(li):
    for i in range(len(li)):
        li[i] = getDecryptSeed(li[i])
    return li

# fungsi untuk merubah list integer sebagai karakter dan sebaliknya
def numListToString(num):
    result = ''
    for i in range(len(num)):
        result += allowedCharacters[num[i]]

    return result

def stringToNumList(strInp):
    strInp = list(strInp)
    
    for j in range(len(strInp)):
        for i in range(len(allowedCharacters)): # change the len
            if allowedCharacters[i] == strInp[j]:
                strInp[j] = i
    return strInp


# fungsi utama
def encrypt(password : str) -> str:
    return numListToString(encryptList(stringToNumList(password)))

def decrypt(password : str) -> str:
    return numListToString(decryptList(stringToNumList(password)))

if __name__ == '__main__':
    inp = input('d or e? : ')
    if inp == 'e':
        pw = input('password : ')
        print(encrypt(pw))
    else :
        pw = input('hashed pw : ')
        print(decrypt(pw))