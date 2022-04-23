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


# DI BAWAH INI JANGAN DULU
def getBoxUI(*boxLen : int, limiter : str = '|') -> str:
    limiter = '|'
    result = limiter
    for i in boxLen:
        result += '{:^i}' + limiter

    return result