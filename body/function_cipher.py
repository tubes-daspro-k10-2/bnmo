from constants import defaultAllowedCharacter
from utils.main import getLength

# uses affine cipher
# seed :
# a = 9
# b = 3

allowedCharacters = defaultAllowedCharacter

aDefault = 9
bDefault = 3
mDefault = getLength(allowedCharacters) # how many alphabets from a - z are


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

def encryptList(li):
    for i in range(len(li)):
        # print(li[i], encrypt(li[i]))
        li[i] = getEncryptSeed(li[i])
    return li

def decryptList(li):
    for i in range(len(li)):
        # print(li[i], decrypt(li[i]))
        li[i] = getDecryptSeed(li[i])
    return li



# print(decrypt(encrypt(0)))
# result : 0



def numListToString(num):
    result = ''
    for i in range(len(num)):
        result += allowedCharacters[num[i]]

    return result
    
    
    return allowedCharacters[num]

def stringToNumList(strInp):
    strInp = list(strInp)
    
    for j in range(len(strInp)):
        for i in range(len(allowedCharacters)): # change the len
            if allowedCharacters[i] == strInp[j]:
                strInp[j] = i
    return strInp

## FInal FUnction
def encrypt(password : str) -> str:
    return numListToString(encryptList(stringToNumList(password)))

def decrypt(password : str) -> str:
    return numListToString(decryptList(stringToNumList(password)))

#print(stringToNumList('as'))
#print(numListToString([0, 2]))
#print(numListToString(stringToNumList('asss')))

#print(numListToString(encryptList(stringToNumList('password'))))

if __name__ == '__main__':
    inp = input('d or e? : ')
    if inp == 'e':
        pw = input('password : ')
        print(encrypt(pw))
    else :
        pw = input('hashed pw : ')
        print(decrypt(pw))