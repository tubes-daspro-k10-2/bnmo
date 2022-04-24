# main util
import time

def getLength(arr : list) -> int:
    # fungsi implementasi ulang len()
    count : int = 0
    for i in arr:
        count += 1
    
    return count

def split(toSplit : str, delimiter : str) -> list[str]:
    # fungsi yang berguna untuk melakukan split

    currentWord = ''
    resultArray = []

    for i in range(len(toSplit)):
        char = toSplit[i]

        # handler untuk end of string
        if i+1 == len(toSplit):
            if char == delimiter:
                resultArray += [currentWord]
                resultArray += ['']
            else:
                currentWord += char                
                resultArray += [currentWord]
                
        # handler untuk non end of string           
        else:
            if char == delimiter :
                resultArray += [currentWord]
                currentWord = ''
            else:
                currentWord += char

    return resultArray

def isGenap(x : int) -> bool: 
    # fungsi yang menentukan apakah masukan bernilai genap

    return x % 2 == 0