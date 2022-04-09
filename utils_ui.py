from utils import *

def header(screenWidth : int = 20):
    printCenter('BNMO', screenWidth)
    printCenter('by K10-2', screenWidth)

def mainChoices():
    print(' 1. Register')
    print(' 2. Login') 
    print(' 3. tambah game')
    print(' 4. ubah game toko')
    print(' 5. ubah stok game')
    print(' 6. list game toko')
    print(' 7. beli game')
    print(' 8. lihat inv game')
    print(' 9. search inv game id tahun')
    print('10. search game toko')
    print('11. top up')
    print('12. riwayat pembelian')
    print('13. help')
    print('14. load')
    print('15. save')
    print('16. exit')

def RegisterPage() -> str :
    printCenter('Register a New User')
    print()
    printCenter('Nama')
    printCenter('┌                    ┐') #maks 20
    name = inputCenter()
    printCenter('Username')
    printCenter('┌                    ┐') #maks 20
    username = inputCenter()
    printCenter('Password')
    printCenter('┌                    ┐') #maks 20
    password = inputCenter()
    
    return name, username, password

# def footer():
#     print('made with love')

################## INPUT #######################
def inputCenter(maxLen : int = 20, screenWidth : int = 100, space : str = ' ') -> str:
    diff = screenWidth - maxLen
    
    if maxLen > screenWidth :
        return input()

    if isGenap(diff):
        return input(int(diff/2) * space)
    else:
        return input(int((diff+1)/2) * space)

################## PRINT #######################
def printCenter(text : str = 'URE MISSING TEXT INPUT', screenWidth : int = 100, space : str = ' '):
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

def printRight(text : str = 'URE MISSING TEXT INPUT', screenWidth : int = 20, space : str = ' '):
    # right align print, parameter : teks masukan, lebar layar, isian space
    textLen = getLength(text)
    diff = screenWidth - textLen

    if textLen > screenWidth :
        print(text)
        return

    print(diff*space + text)

def printBlock(char : str = '#', screenWidth : int = 20):
    print(char*screenWidth)

def printWarning(text : str = 'URE MISSING TEXT INPUT', screenWidth : int = 20, space : str = ' '):
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