from constants import defaultScreenWidth
from utils.ui import inputValidated, printCenter, printRight, inputCenter, clearScreen

def header(screenWidth : int = defaultScreenWidth):
    printCenter('BNMO', screenWidth)
    printCenter('by K10-2', screenWidth)

def printAccount(sessionAccount : list):
    printRight(sessionAccount[0])
    printRight(sessionAccount[1])
    printRight('Rp ' + str(sessionAccount[2]))

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

def LandingPage() -> str:
    printCenter('Welcome!')
    print()
    print()
    printCenter('1. Login   ')
    printCenter('2. Register')
    print()
    printCenter('3. Exit    ')

    
    try:
        ans = inputValidated('>>> ', ['1', '2', '3', 'login', 'register', 'exit'])
    except:
        pass
    if ans == '1' or ans.lower() == 'login':
        return 1
    elif ans == '2' or ans.lower() == 'register':
        return 2
    else: # 3 or exit
        return 3

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

def LoginPage():
    pass

def MainMenu(sessionAccount : list):
    printCenter('Main Menu')

    # account info
    printAccount(sessionAccount)
    print()

    mainChoices()
    print()
    dummiinput = input('Masukkan perintah : ')

    return dummiinput
    
