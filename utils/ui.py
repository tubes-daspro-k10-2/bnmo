from utils.main import isGenap, getLength
from constants import defaultScreenWidth, defaultAllowedCharacter
from os import system, name

################## INPUT #######################
def inputCenter(maxLen : int = 20, screenWidth : int = defaultScreenWidth, space : str = ' ') -> str:
    # fungsi untuk meminta masukan dengan menengahkan kolom masukan

    diff = screenWidth - maxLen
    
    if maxLen > screenWidth :
        return input()

    if isGenap(diff):
        return input(int(diff/2) * space)
    else:
        return input(int((diff+1)/2) * space)

def inputValidated(text : str = '', validInput : list = defaultAllowedCharacter) -> str:
    # fungsi untuk meminta masukan dengan membatasi masukan hanya boleh anggota validInput

    finished = False
    while not finished:
        try:
            ans = str(input(text))
        except:
            pass

        if ans.lower() in validInput:
            finished = True
    
    return ans

def validIntegerInput(textInput : str = '', lowerLimit : int = '' ):
    # fungsi yang memvalidasi masukan sebagai integer sampai berhasil

    while True:
        ans = input(textInput)
        try:
            if ans == '':
                return ans
            ans = int(ans)
        except:
            print()
            print('Input bukan bilangan bulat!')
            print()
        else:
            if lowerLimit != '':
                if not lowerLimit < ans:
                    print('Nilai tidak boleh kurang dari', lowerLimit)
                else:
                    return ans
            else:
                return ans

def validStringInput(textInput : str = '', bannedCharacters : list = [';', ' ']):
    # fungsi yang memvalidasi masukan hingga bernilai string dengan memperhatikan karakter yang tidak diperbolehkan

    while True:
        try:
            ans = (input(textInput))
        except:
            pass
        else:
            valid = True
            for i in ans:
                for j in bannedCharacters:
                    if i == j:
                        valid = False
                        print('Masukan tidak valid')
                        break
            
            if valid:
                return ans
            

################## PRINT #######################
def printCenter(text : str = 'URE MISSING TEXT INPUT', screenWidth : int = defaultScreenWidth, space : str = ' '):
    # center align print, parameter : teks masukan, lebar layar, isian space

    textLen = getLength(text)
    diff = screenWidth - textLen

    if textLen > screenWidth :
        print(text)
        return

    if isGenap(diff):
        print(int(diff/2) * space + text + int(diff/2) * space)
    else:
        print(int((diff+1)/2) * space + text + int((diff-1)/2) * space)

def printRight(text : str = 'URE MISSING TEXT INPUT', screenWidth : int = defaultScreenWidth, space : str = ' '):
    # right align print, parameter : teks masukan, lebar layar, isian space

    textLen = getLength(text)
    diff = screenWidth - textLen

    if textLen > screenWidth :
        print(text)
        return

    print(diff*space + text)

def printBlock(char : str = '#', screenWidth : int = defaultScreenWidth):
    # fungsi untuk mengblock satu baris dengan karakter yang dimasukkan

    print(char*screenWidth)

def printWarning(text : str = 'URE MISSING TEXT INPUT', screenWidth : int = defaultScreenWidth, space : str = ' '):
    # center align print, parameter : teks masukan, lebar layar, isian space
    textLen = getLength(text)
    diff = screenWidth - textLen

    textToPrint = text

    if textLen > screenWidth :
        textToPrint = text
    else:
        if isGenap(diff):
            textToPrint = (int(diff/2) * space + text + int(diff/2) * space)
        else:
            textToPrint = (int((diff+1)/2) * space + text + int((diff-1)/2) * space)
    print()
    printBlock(screenWidth=screenWidth)
    printCenter(textToPrint, screenWidth)
    printBlock(screenWidth=screenWidth)
    print()

def clearScreen():
    # fungsi untuk membersihkan layar

    if name == 'nt': # merupakan sistem windows
        _ = system('cls')
  
    else:           # bukan sistem windows
        _ = system('clear')

# UI Box
def getBoxUI(boxLen : list, limiter : str = '|', isHeader : bool = False) -> str:
    # formatting string untuk membuat box daftar item, memperhatikan panjang yang diinginkan

    limiter = '|'
    result = limiter
    for i in boxLen:
        if not isHeader:
            result += '{:<'+ str(i) +'}' + limiter
        else:
            result += '{:^'+ str(i) +'}' + limiter

    return result

def makeBoxUI(arr : list[list], header : list = ''):

    # jika masukan adalah list kosong
    if getLength(arr) == 0:
        return

    print()
    # matriks kosong yang menyimpan panjang yang diinginkan
    contentArr = [['' for i in range(getLength(arr[j]))] for j in range (getLength(arr))]
    lengthArr = [0 for i in arr[0]]

    for i in range(getLength(contentArr)):
        for j in range(getLength(contentArr[i])):
            contentArr[i][j] = arr[i][j]

    # iterasi data yang bersesuaian indeks, dan cari data dengan panjang string terpanjang    
    for i in range(getLength(contentArr)):
        for j in range(getLength(contentArr[i])):
            if lengthArr[j] < getLength(str(contentArr[i][j])) or lengthArr[j] < getLength(str(header[j])):
                if getLength(str(contentArr[i][j])) > getLength(str(header[j])):
                    lengthArr[j] = getLength(str(contentArr[i][j]))
                else:
                    lengthArr[j] = getLength(str(header[j]))

    # beri margin di kiri dan kanan teks
    for i in range(getLength(lengthArr)):
        lengthArr[i] += 2

    for i in range(getLength(contentArr)):
        for j in range(getLength(contentArr[i])):
            contentArr[i][j] = ' ' + str(contentArr[i][j])


    # cetak header untuk daftar item
    if header != '':
        print(getBoxUI(lengthArr, isHeader=True).format(*tuple(header)))    

    # cetak daftar item dengan format yang memperhatikan masukan panjang yang telah didapat
    for i in range(getLength(contentArr)):
        print(getBoxUI(lengthArr).format(*tuple(contentArr[i])))

