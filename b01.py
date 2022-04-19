# uses affine cipher
# seed :
# a = 9
# b = 3

aDefault = 9
bDefault = 3
mDefault = 26 # how many alphabets from a - z are


# modular multiplicative inverse a^-1 is
# 1 = a*a^-1 mod m

def getMMI(x, m = mDefault):
    xInverse = 0
    while (xInverse * x % m != 1):
        xInverse += 1
    
    return xInverse

# affine cipher

def encrypt(x, a = aDefault, b = bDefault, m = mDefault):
    return (a*x + b) % m

def decrypt(x, a=aDefault, b = bDefault, m = mDefault):
    return getMMI(a) * (x - b) % m

def encryptList(li):
    for i in range(len(li)):
        # print(li[i], encrypt(li[i]))
        li[i] = encrypt(li[i])
    return li

def decryptList(li):
    for i in range(len(li)):
        # print(li[i], decrypt(li[i]))
        li[i] = decrypt(li[i])
    return li



# print(decrypt(encrypt(0)))
# result : 0

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def numListToString(num):
    result = ''
    for i in range(len(num)):
        result += alphabets[num[i]]

    return result
    
    
    return alphabets[num]

def stringToNumList(strInp):
    strInp = list(strInp)
    
    for j in range(len(strInp)):
        for i in range(len(alphabets)): # change the len
            if alphabets[i] == strInp[j]:
                strInp[j] = i
    return strInp

#print(stringToNumList('as'))
#print(numListToString([0, 2]))
#print(numListToString(stringToNumList('asss')))

#print(numListToString(encryptList(stringToNumList('password'))))

inp = input('d or e? : ')
if inp == 'e':
    pw = input('password : ')
    print(numListToString(encryptList(stringToNumList(pw))))
else :
    pw = input('hashed pw : ')
    print(numListToString(decryptList(stringToNumList(pw))))