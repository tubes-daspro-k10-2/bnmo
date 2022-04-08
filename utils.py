# main util
import time

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

# cara pernggunaan persis dengan Random.RandInt
def lcgInt(minInt : int = 0, maxInt : int = 1) -> int:
    seedInt = (time.monotonic()) # might as well times this by 3
    x = seedInt
    a = 3
    c = 1
    m = 7 # changeable, found that the optimal value is 7
   
    lcgResult = int(((a*x)+c) % m ) + 1

    return int(lerp(minInt, maxInt, lcgResult/m)) # lcgResul that is lerp-ed to a and b
    # print(LCG)
    # print(time.monotonic())

def lerp(a, b, t)   :
    return (t*(b-a)+a)