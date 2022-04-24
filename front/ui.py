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

    bonusGameChoices()

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

    bonusGameChoices()

def helpText(sessionAccount : list):
    if isAdmin(sessionAccount):
        print(' 1. register - melakukan registrasi user baru') 
        print(' 2. tambah_game - menambahkan game ke toko')
        print(' 3. ubah_game - mengubah informasi game yang ada di toko')
        print(' 4. ubah_stok - mengubah stok game yang ada di toko')
        print(' 5. list_game_toko - mendaftar semua game yang ada di toko')
        print(' 6. search_game_at_store - mencari game yang ada di toko dengan kriteria tertentu')
        print(' 7. topup - melakukan top up saldo')
        print()
        print(' 8. help - menampilkan menu bantuan ini')
        print(' 9. save - melakukan penyimpanan data')
        print('10. exit - keluar dari aplikasi')
        print()
        print('11. kerangajaib - beri pertanyaan dan kerang ajaib akan menjawabnya!')
        print('12. tictactoe - main tictactoe bersama dengan teman mu')
    else:
        print(' 1. list_game_toko - mendaftar semua game yang ada di toko')
        print(' 2. buy_game - membeli game yang ada di toko menggunakan saldo yang dimiliki')
        print(' 3. list_game - mendaftar game yang sudah dimiliki')
        print(' 4. search_my_game - mencari game yang sudah dimiliki dengan kriteria tertentu')
        print(' 5. search_game_at_store - mencari game yang ada di toko dengan kriteria tertentu')
        print(' 6. riwayat - melihat riwayat pembelian yang sudah dilakukan')
        print()
        print(' 8. help - menampilkan menu bantuan ini')
        print(' 9. save - melakukan penyimpanan data')
        print('10. exit - keluar dari aplikasi')
        print()
        print('11. kerangajaib - beri pertanyaan dan kerang ajaib akan menjawabnya!')
        print('12. tictactoe - main tictactoe bersama dengan teman mu')

def bonusGameChoices():
    print()
    print('11. kerangajaib')
    print('12. tictactoe')

def LandingPage() -> int:
    printCenter('Welcome!')
    print()
    print()
    printCenter('1. Login   ')
    # printCenter('2. Register')
    print()
    printCenter('2. Exit    ')

    
    try:
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
    print()
    print()
    printCenter('Login to an existing Account')
    print()
    printCenter('Username')
    printCenter('┌                    ┐') #maks 20
    username = inputCenter()
    printCenter('Password')
    printCenter('┌                    ┐') #maks 20
    password = inputCenter()
    print()
    print()
    
    return username, password

def MainMenu(sessionAccount : list) -> int:
    printCenter('Main Menu')

    # account info
    printAccount(sessionAccount)
    print()

    if isAdmin(sessionAccount):
        adminChoices()
        print()
        try:
            choiceAnswer = inputValidated('>>> ', ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
            'register', 'tambah_game', 'ubah_game', 'ubah_stok', 'list_game_toko', 'search_game_at_store', 'topup', 'help', 'save', 'exit',
            '11', '12', 'kerangajaib', 'tictactoe'])
            print()
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

        elif choiceAnswer == '11' or choiceAnswer == 'kerangajaib':
            return 11
        elif choiceAnswer == '12' or choiceAnswer == 'tictactoe':
            return 12

    else:
        userChoices()
        print()
        try:
            choiceAnswer = inputValidated('>>> ', ['1', '2', '3', '4', '5', '6', '8', '9', '10', 
            'list_game_toko', 'buy_game', 'list_game', 'search_my_game', 'search_game_at_store', 'riwayat', 'help', 'save', 'exit',
            '11', '12', 'kerangajaib', 'tictactoe' ])
            print()
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

        elif choiceAnswer == '11' or choiceAnswer == 'kerangajaib':
            return 11
        elif choiceAnswer == '12' or choiceAnswer == 'tictactoe':
            return 12

    print()

    
    return choiceAnswer

def ExitPage():
    printCenter('Thank You!')
    print()
    printCenter('Made with love by us K10-2! ♥')