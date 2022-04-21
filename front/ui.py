from constants import defaultScreenWidth
from utils.ui import inputValidated, printCenter, printRight, inputCenter, clearScreen
from utils.user import isAdmin

def header(screenWidth : int = defaultScreenWidth):
    printCenter('BNMO', screenWidth)
    printCenter('by K10-2', screenWidth)

def printAccount(sessionAccount : list):
    printRight(sessionAccount[0])
    printRight(sessionAccount[1])
    printRight('Rp ' + str(sessionAccount[2]))

def userChoices():
    print(' 1. list_game_toko')
    print(' 2. beli_game')
    print(' 3. lihat_game_toko')
    print(' 4. cari_game_dimiliki')
    print(' 5. cari_game_toko')
    print(' 6. riwayat_pembelian')
    
    print(' 8. help')
    print(' 9. save')
    print('10. exit')

def adminChoices():
    print(' 1. register') 
    print(' 2. tambah_game_toko')
    print(' 3. ubah_game_toko')
    print(' 4. ubah_stok_game_toko')
    print(' 5. list_game_toko')
    print(' 6. cari_game_toko')
    print(' 7. top_up')

    print(' 8. help')
    print(' 9. save')
    print('10. exit')

# def userChoices():
#     print(' 1. List Game di Toko')
#     print(' 2. Beli Game')
#     print(' 3. Lihat Game yang Dimiliki')
#     print(' 4. Cari Game yang Dimiliki')
#     print(' 5. Cari Game di Toko')
#     print(' 6. Lihat Riwayat Pembelian')
    
#     print(' 8. Help')
#     print(' 9. Save')
#     print('10. Exit')

# def adminChoices():
#     print(' 1. Register') 
#     print(' 2. Tambah Game ke Toko')
#     print(' 3. Ubah Game di Toko')
#     print(' 4. Ubah Stok Game di Toko')
#     print(' 5. List Game di Toko')
#     print(' 6. Cari Game di Toko')
#     print(' 7. Top Up Saldo')

#     print(' 8. Help')
#     print(' 9. Save')
#     print('10. Exit')



def LandingPage() -> int:
    printCenter('Welcome!')
    print()
    print()
    printCenter('1. Login   ')
    # printCenter('2. Register')
    print()
    printCenter('2. Exit    ')

    
    try:
        # ans = inputValidated('>>> ', ['1', '2', '3', 'login', 'register', 'exit'])
        choiceAnswer = inputValidated('>>> ', ['1', '2', 'login', 'exit'])
    except:
        pass
    if choiceAnswer == '1' or choiceAnswer.lower() == 'login':
        return 1
    # elif ans == '2' or ans.lower() == 'register':
    #     return 2
    else: # 3 or exit
        return 2

def RegisterPage() -> list[str, str, str] :
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

def LoginPage() -> tuple[str, str]:
    printCenter('Login to an existing Account')
    print()
    printCenter('Username')
    printCenter('┌                    ┐') #maks 20
    username = inputCenter()
    printCenter('Password')
    printCenter('┌                    ┐') #maks 20
    password = inputCenter()
    
    return username, password

def MainMenu(sessionAccount : list) -> int:
    printCenter('Main Menu')

    # account info
    printAccount(sessionAccount)
    print()

    if isAdmin(sessionAccount):
        adminChoices()

        try:
            choiceAnswer = inputValidated('Masukkan perintah : ', ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
            'register', 'tambah_game_toko', 'ubah_game_toko', 'ubah_stok_game_toko', 'list_game_toko', 'cari_game_toko', 'top_up', 'help', 'save', 'exit'])
        except:
            pass
        
        if choiceAnswer == '1' or choiceAnswer == 'register':
            return 1
        elif choiceAnswer == '2' or choiceAnswer == 'tambah_game_toko':
            return 2
        elif choiceAnswer == '3' or choiceAnswer == 'ubah_game_toko':
            return 3
        elif choiceAnswer == '4' or choiceAnswer == 'ubah_stok_game_toko':
            return 4
        elif choiceAnswer == '5' or choiceAnswer == 'list_game_toko':
            return 5
        elif choiceAnswer == '6' or choiceAnswer == 'cari_game_toko':
            return 6
        elif choiceAnswer == '7' or choiceAnswer == 'top_up':
            return 7

        elif choiceAnswer == '8' or choiceAnswer == 'help':
            return 8
        elif choiceAnswer == '9' or choiceAnswer == 'save':
            return 9
        elif choiceAnswer == '10' or choiceAnswer == 'exit':
            return 10


    else:
        userChoices()

        try:
            choiceAnswer = inputValidated('Masukkan perintah : ', ['1', '2', '3', '4', '5', '6', '8', '9', '10', 
            'list_game_toko', 'beli_game', 'lihat_game_toko', 'cari_game_dimiliki', 'cari_game_toko', 'riwayat_pembelian', 'help', 'save', 'exit' ])
        except:
            pass

        if choiceAnswer == '1' or choiceAnswer == 'list_game_toko':
            return 1
        elif choiceAnswer == '2' or choiceAnswer == 'beli_game':
            return 2
        elif choiceAnswer == '3' or choiceAnswer == 'lihat_game_toko':
            return 3
        elif choiceAnswer == '4' or choiceAnswer == 'cari_game_dimiliki':
            return 4
        elif choiceAnswer == '5' or choiceAnswer == 'cari_game_toko':
            return 5
        elif choiceAnswer == '6' or choiceAnswer == 'riwayat_pembelian':  
            return 6

        elif choiceAnswer == '8' or choiceAnswer == 'help':
            return 8
        elif choiceAnswer == '9' or choiceAnswer == 'save':
            return 9
        elif choiceAnswer == '10' or choiceAnswer == 'exit':
            return 10
    print()

    
    return choiceAnswer
