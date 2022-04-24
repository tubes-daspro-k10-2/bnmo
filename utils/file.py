import os
from utils.main import split, getLength
from utils.ui import printWarning
from constants import usercsvHeader, gamecsvHeader, kepemilikancsvHeader, riwayatcsvHeader

def folderExist(folderArg : str) -> bool :
    # apakah folder ada 

    for (root, dirs, files) in os.walk(folderArg, topdown=True): #melakukan walk ke folder dan mendapati kalau salah satu folder namanya sama dengan yang diinginkan
        if root == folderArg: 
            return True
    return False #jika tidak ditemukan nama folder yang dimaksud

def createFolder(folderArg : str):
    # buat folder dengan nama yang diinpput
    os.makedirs(folderArg)
    print(folderArg, 'created.')

def read_csv(folderPath : str, fileName : str) -> list[str]:
    resultArray = [] # arr kosong

    with open(str(folderPath)+str(fileName)+'.csv') as f:
        file = f.read()
        #print(file)
        
        file = split(file, '\n') # split, menggunakan fungsi yang dibuat sendiri, lihat utils.main

        for i in range(getLength(file)): # split by escape character '\n'
            if i != 0: # jika bukan header, ambil data saja
                resultArray += [file[i]]

    for i in range(getLength(resultArray)):
        resultArray[i] = split(resultArray[i], ';') # potong string yang dibatasi tanda (;) menjadi list baru
        
    # catch file kosong
    if resultArray == [] or resultArray == [[]]:
        lenNeeded = 0
        if fileName == 'kepemilikan':
            lenNeeded = getLength(kepemilikancsvHeader)
        elif fileName == 'riwayat':
            lenNeeded = getLength(riwayatcsvHeader)
        elif fileName == 'game':
            lenNeeded = getLength(gamecsvHeader)
        
        emptyContent = []
        for i in range(lenNeeded):
            emptyContent += [[]]
        print(emptyContent)
        return emptyContent

    return resultArray

def append_array(arr : list, toAppend : list, konso : bool = True) -> list:
    # tambahkan list ke array, 
    # parameter boolean konso -> True, maka fungsi menjadi konso; False, fungsi menjadi konsDot
    
    if arr == [] or getLength(arr[0]) != getLength(toAppend): # jika array awal kosong atau anggota array dan list yang akan dimasukkan tidak memiliki panjang yang sama
        printWarning('DIFFERENT LIST SIZE') 

    if konso:
        arr = arr + [toAppend] # lakukan konso
    else:
        arr = [toAppend] + arr # lakukan konsDot

    return arr

def update_array(arr: list, fileName : str) -> list:
    # fungsi yang mengembalikan header kembali ke dalam array sebelum dilakukan penyimpanan

    if fileName == 'user':
        arr = append_array(arr, usercsvHeader, False)
    elif fileName == 'game':
        arr = append_array(arr, gamecsvHeader, False)
    elif fileName == 'riwayat':
        arr = append_array(arr, riwayatcsvHeader, False)
    else: #fileName == 'kepemilikan':
        arr = append_array(arr, kepemilikancsvHeader, False)

    return arr

def list_to_csv(content : list) -> str:
    # fungsi yang akan memformat list sebagai string yang dibatasi tanda (;) sebelum dilakukan penyimpanan

    newCsvLine : str = ''
    for i in range(len(content)):
        newCsvLine += str(content[i])
        if i+1 != len(content) :
            newCsvLine += ';'
    return newCsvLine


def save_csv(folderPath : str, fileName : str, content : list[str]):
    
    # tambahkan header kembali
    content = update_array(content, fileName) 

    newContent = ['' for i in content] # empty list

    # format kembali list menjadi string
    for i in range(getLength(newContent)):
        newContent[i] = list_to_csv(content[i]) 

    # simpan string ke dalam csv
    with open(str(folderPath)+str(fileName)+'.csv', 'w+') as f:
        for i in range(getLength(newContent)):
            f.write(newContent[i])
            if i+1 < getLength(newContent):
                f.write('\n')

def getIndexByName(indexName : str, fileName : str) -> int:
    # fungsi yang berguna untuk memberi index dari suatu anggota dari header sesuai dengan nama file masukan

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
    else: #fileName == 'kepemilikan'
        for i in range(getLength(kepemilikancsvHeader)):
            if indexName == kepemilikancsvHeader[i]:
                return i