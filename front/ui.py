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
    print(' 2. buy_game')
    print(' 3. list_game')
    print(' 4. search_my_game')
    print(' 5. search_game_at_store')
    print(' 6. riwayat')
    print()
    print(' 8. help')
    print(' 9. save')
    print('10. exit')

def adminChoices():
    print(' 1. register') 
    print(' 2. tambah_game')
    print(' 3. ubah_game')
    print(' 4. ubah_stok')
    print(' 5. list_game_toko')
    print(' 6. search_game_at_store')
    print(' 7. topup')
    print()
    print(' 8. help')
    print(' 9. save')
    print('10. exit')

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
            'register', 'tambah_game', 'ubah_game', 'ubah_stok', 'list_game_toko', 'search_game_at_store', 'topup', 'help', 'save', 'exit'])
        except:
            pass
        
        if choiceAnswer == '1' or choiceAnswer == 'register':
            return 1
        elif choiceAnswer == '2' or choiceAnswer == 'tambah_game':
            return 2
        elif choiceAnswer == '3' or choiceAnswer == 'ubah_game':
            return 3
        elif choiceAnswer == '4' or choiceAnswer == 'ubah_stok':
            return 4
        elif choiceAnswer == '5' or choiceAnswer == 'list_game_toko':
            return 5
        elif choiceAnswer == '6' or choiceAnswer == 'search_game_at_store':
            return 6
        elif choiceAnswer == '7' or choiceAnswer == 'topup':
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
            'list_game_toko', 'buy_game', 'list_game', 'search_my_game', 'search_game_at_store', 'riwayat', 'help', 'save', 'exit' ])
        except:
            pass

        if choiceAnswer == '1' or choiceAnswer == 'list_game_toko':
            return 1
        elif choiceAnswer == '2' or choiceAnswer == 'buy_game':
            return 2
        elif choiceAnswer == '3' or choiceAnswer == 'list_game':
            return 3
        elif choiceAnswer == '4' or choiceAnswer == 'search_my_game':
            return 4
        elif choiceAnswer == '5' or choiceAnswer == 'search_game_at_store':
            return 5
        elif choiceAnswer == '6' or choiceAnswer == 'riwayat':  
            return 6

        elif choiceAnswer == '8' or choiceAnswer == 'help':
            return 8
        elif choiceAnswer == '9' or choiceAnswer == 'save':
            return 9
        elif choiceAnswer == '10' or choiceAnswer == 'exit':
            return 10
    print()

    
    return choiceAnswer

def ExitPage():
    printCenter('Thank You!')
    print()
    printCenter('Made with love by us K10-2! ♥')