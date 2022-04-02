# main util

def len(arr : list) -> int:
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

def getListHead(arr : list) -> any:
    return arr[0]

def getListTail(arr: list) -> list[any] :
    resultArray = []

    for i in range(1, len(arr)):
        resultArray += [arr[i]]

    return resultArray

def tokenize(key : list, value : list) -> dict[any, any]:

    # buat dict dari 2 list
    pairs : list[tuple] = []

    for i in range(len(key)):
        pairs += [(key[i], value[i])]

    return {k : v for k, v in pairs}



'''
    print(split(input(), ','))
parsedcsv = parse_csv('lmao.csv')
print(parsedcsv)
print(parsedcsv[2]['key1'])



'''
