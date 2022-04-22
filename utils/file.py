from fileinput import filename
import os
from utils.main import split, getLength
from utils.ui import printWarning
from constants import usercsvHeader, gamecsvHeader, kepemilikancsvHeader, riwayatcsvHeader

def folderExist(folderArg : str) -> bool :
    for (root, dirs, files) in os.walk(folderArg, topdown=True):
        if root == folderArg:
            return True
    return False

def createFolder(folderArg : str):
    os.makedirs(folderArg)
    print(folderArg, 'created.')

def read_csv(folderPath : str, fileName : str) -> list[str]:
    resultArray = []

    with open(str(folderPath)+str(fileName)+'.csv') as f:
        file = f.read()
        #print(file)
        
        file = split(file, '\n')

        for i in range(getLength(file)): # split by escape character '\n'
            if i != 0: # solusi sementara, need some nganu like strip or sth
                resultArray += [file[i]]

    for i in range(getLength(resultArray)):
        resultArray[i] = split(resultArray[i], ';')

    return resultArray

def append_array(arr : list, toAppend : list, konso : bool = True) -> list:
    # newData : list = [str(i) for i in values]
    
    if arr == [] or getLength(arr[0]) != getLength(toAppend):
        printWarning('DIFFERENT LIST SIZE')
    #print(type(arr), type(newData))
    # for i in range(len(values)):
    #     newData += str(values[i])
    #     if i+1 != len(values) :
    #         newData += ';'
    if konso:
        arr = arr + [toAppend] # sub array
    else:
        arr = [toAppend] + arr
    
    # arr = update_array(arr) # removed it in now
    print(arr)
    #print('util file', arr)#

    return arr

def update_array(arr: list, fileName : str) -> list:
    for i in range(getLength(arr)):
        #arr[i][0] = i+1
        pass
    
    if fileName == 'user':
        arr = [usercsvHeader] + arr
    elif fileName == 'game':
        arr = [gamecsvHeader] + arr
    elif fileName == 'riwayat':
        arr = [riwayatcsvHeader] + arr
    else: #fileName == 'kepemilikan':
        arr = [kepemilikancsvHeader] + arr

    return arr

def list_to_csv(content : list) -> str:
    newCsvLine : str = ''
    #print('ctn1:', content)
    for i in range(len(content)):
        newCsvLine += str(content[i])
        if i+1 != len(content) :
            newCsvLine += ';'
    #print('ctn2', newCsvLine)
    return newCsvLine


def save_csv(folderPath : str, fileName : str, content : list[str]):
    # print(folderPath, fileName)
    # print(getLength(content))
    
    content = update_array(content, fileName)

    newContent = ['' for i in content] # empty list

    for i in range(getLength(newContent)):
        newContent[i] = list_to_csv(content[i])

    

    print('filepy', newContent)

    with open(str(folderPath)+str(fileName)+'.csv', 'w+') as f:
        # print(getlength(content))
        for i in range(getLength(newContent)):
            # print(content[i], getLength(content))
            # print(i)
            f.write(newContent[i])
            if i+1 < getLength(newContent):
                f.write('\n')

def getIndexByName(indexName : str, fileName : str) -> int:
    if fileName == 'user':
        for i in range(getLength(usercsvHeader)):
            if indexName == usercsvHeader[i]:
                return i
    elif fileName == 'game':
        for i in range(getLength(gamecsvHeader)):
            if indexName == gamecsvHeader[i]:
                return i
    elif fileName == 'riwayat':
        for i in range(getLength(riwayatcsvHeader)):
            if indexName == riwayatcsvHeader[i]:
                return i
    else: #fileName == 'kepemilikan':
        for i in range(getLength(kepemilikancsvHeader)):
            if indexName == kepemilikancsvHeader[i]:
                return i
        