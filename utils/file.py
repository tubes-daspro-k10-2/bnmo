import os
from f02 import getlength
from utils.main import split, getLength

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

        for i in split(file, '\n'): # split by escape character '\n'
            if i != '': # solusi sementara, need some nganu like strip or sth
                resultArray += [i]

    for i in range(getLength(resultArray)):
        resultArray[i] = split(resultArray[i], ';')

    return resultArray

def append_array(arr : list, *values) -> list:
    newData : list = [str(i) for i in values]
    #print(type(arr), type(newData))
    # for i in range(len(values)):
    #     newData += str(values[i])
    #     if i+1 != len(values) :
    #         newData += ';'
    arr += [newData] # sub array

    arr = update_array(arr)

    #print('util file', arr)#

    return arr

def update_array(arr: list) -> list:
    for i in range(getLength(arr)):
        arr[i][0] = i

    return arr


# def append_array(path : str, fileName : str, *values) -> list:
#     data = read_csv(path, fileName)
#     newData : list = [str(i) for i in values]
    
#     print(data) #
#     # for i in range(len(values)):
#     #     newData += str(values[i])
#     #     if i+1 != len(values) :
#     #         newData += ';'
#     data += [newData]

#     print(data)#

#     return data

#need revamp
# def make_csv(path : str, fileName : str, *values):
#     data = read_csv(path, fileName)
#     newData : str = ''

#     for i in range(len(values)):
#         newData += str(values[i])
#         if i+1 != len(values) :
#             newData += ';'
#     data += [newData]
    
#     save_csv(path, fileName, data)
    #update_csv(path)

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
    for i in range(getLength(content)):
        content[i] = list_to_csv(content[i])

    with open(str(folderPath)+str(fileName)+'.csv', 'w+') as f:
        # print(getlength(content))
        for i in range(getLength(content)):
            # print(content[i], getLength(content))
            # print(i)
            f.write(content[i])
            if i+1 < getLength(content):
                f.write('\n')




        

# def parse(path : str) -> list :
#     # array dengan anggota string tiap baris
#     lines : list[str] = readlines(path)

#     # definisi key dictionary
#     keys = split(getListHead(lines), ';')

#     # definisi tiap value yang ada pada key dan buat dictionary
#     tail = getListTail(lines)
    
#     dicts = []

#     for i in range(len(tail)):
#         values = split(tail[i], ';')

#         dicts += [tokenize(keys, values)]

#     return dicts

def parse(path : str) -> list :
    lines : list[str] = read_csv(path)

    for i in range(getLength(lines)):
        lines[i] = split(lines[i], ';')
        
    return lines

#known error : read buat 1 baris yang ga jelas, by excel si
#print(read_csv('./eksperimen/user.csv'))