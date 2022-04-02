# dealing with files
from utility import *

def update_csv(path : str):
    data = readlines(path)
    #print(data)

    for i in range(len(data)):
        newData=''
        if i != 0:
            newData = split(data[i], ';')
            print('nd : ', newData)
            newData[0] = str(i)

        dataStr = ''
        for j in range(len(newData)):
            dataStr+=newData[j]

            if j+1 != len(newData):
                dataStr+=';'


        data[i] = dataStr
    
    #print(data)

    rewrite_csv(path, data)

def readlines(path : str) -> list[str]:
    resultArray = []

    with open(path) as f:
        file = f.read()
        #print(file)

        for i in split(file, '\n'): # split by escape character '\n'
            if i != '': # solusi sementara, need some nganu like strip or sth
                resultArray += [i]

    return resultArray

def write_csv(path : str, *values):
    data = readlines(path)
    newData : str = ''

    for i in range(len(values)):
        newData += str(values[i])
        if i+1 != len(values) :
            newData += ';'
    data += [newData]
    
    rewrite_csv(path, data)
    update_csv(path)

def rewrite_csv(path : str, content : list[str]):
    with open(path, 'r+') as f:
        f.seek(0)
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
    lines : list[str] = readlines(path)

    for i in range(len(lines)):
        lines[i] = split(lines[i], ';')
        
    return lines

#known error : read buat 1 baris yang ga jelas, by excel si

#writeline('lmao.csv', 'adad','asda','sus af')