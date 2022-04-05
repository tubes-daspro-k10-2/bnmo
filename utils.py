
# main util

def getLength(arr : list) -> int:
    count : int = 0
    for i in arr:
        count += 1
    
    return count

def split(toSplit : str, delimiter : str) -> list[str]:
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
                
        # handler untuk the rest           
        else:
            if char == delimiter :
                resultArray += [currentWord]
                currentWord = ''
            else:
                currentWord += char

    return resultArray

def isGenap(x : int) -> bool: 
    return x % 2 == 0