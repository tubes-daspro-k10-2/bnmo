import os
from utils import *

def folderExist(folderArg : str) -> bool :
    for (root, dirs, files) in os.walk(folderArg, topdown=True):
        if root == folderArg:
            return True
        
    return False

def read_csv(folderPath : str, fileName : str) -> list[str]:
    resultArray = []

    with open(str(folderPath)+str(fileName)+'.csv') as f:
        file = f.read()
        #print(file)

        for i in split(file, '\n'): # split by escape character '\n'
            if i != '': # solusi sementara, need some nganu like strip or sth
                resultArray += [i]

    return resultArray

#need revamp
def make_csv(path : str, fileName : str, *values):
    data = read_csv(path, fileName)
    newData : str = ''

    for i in range(len(values)):
        newData += str(values[i])
        if i+1 != len(values) :
            newData += ';'
    data += [newData]
    
    write_csv(path, fileName, data)
    #update_csv(path)

def write_csv(folderPath : str, fileName, content : list[str]):
    with open(str(folderPath)+str(fileName)+'.csv', 'w+') as f:
        for i in content:
            print(i)
            f.write(i + '\n')

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