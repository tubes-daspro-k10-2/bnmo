from utils.file import append_array, read_csv, folderExist, createFolder, save_csv
from utils.ui import printWarning
from utils.user import isUsernameValid
from utils.main import getLength

from body.function_cipher import encrypt, decrypt

from constants import emptySessionAccount

#f02
def register(userArray, nama, username, password) -> list[str, str, str, str]:
    #user = data[0]
    #=====================INPUT DATA===================
    user_valid = False
    while (not user_valid):
        # nama = input("Masukan nama: ")
        # username = input("Masukan username: ")
        # password = input("Masukan password: ")
        
        terdaftar = False
        i = 0
        while ((not terdaftar) and i < getLength(userArray)):
            if (userArray[i][1] == username):
                print("\nUsername ",username," sudah terpakai, silakan menggunakan username lain.")
                terdaftar = True
            i+=1
        if (not terdaftar):
            if (isUsernameValid(username)):
                user_valid = True
            else:
                print("Username hanya dapat mengandung alfabet A-Z a-z, underscore '_', strip '-', dan angka 0-9") 
            
    
    #======================TAMBAHKAN DATA BARU===================
    idn = getLength(userArray)

    hashedPassword = encrypt(password) ## cipher

    baru = [str(idn),username,nama,hashedPassword,"user",0] #id,username,name,password,role,saldo
    # temp = [0 for i in range (getLength(userArray)+1)]
    # for i in range (getLength(userArray)):
    #     temp[i] = userArray[i]
    # temp[getLength(userArray)] = baru

    userArray = append_array(userArray, baru)

    
    #sukses didaftarkan
    print("\nUsername ",username,' telah berhasil register ke dalam "Binomo"')

    return userArray

#f03
def login(userArray : list, username : str, password : str) -> list[str, str, str, str]:
    hashedPassword = encrypt(password)
    print('has', hashedPassword)
    print('unhas', decrypt(hashedPassword))
    ada = False
    i=0
    while ((not ada) and i < getLength(userArray)):
        if (userArray[i][1] == username and userArray[i][3]==hashedPassword):
            print("\nHalo ", username, "! Selamat datang di Binomo.")
            ada = True
            
            # tangkep nilainya di main
            return userArray[i][1], userArray[i][2], userArray[i][5], userArray[i][4] #username, name, saldo, role       
        i += 1

    print("\nMasukan username atau password salah atau tidak ditemukan")

    return emptySessionAccount

#f04
def tambah_game(gameArray : list) -> list:
    #g.login = True
    #g.role = "Admin"
    valid = False
    while (not valid):
        print()
    #========INPUT DATA GAME BARU===========================

        try:
            nama = input("Masukkan nama game : ")
            kategori = input("Masukkan kategori : ")
            tahun_rilis = int(input("Masukkan tahun rilis : "))
            harga = int(input("Masukkan harga: "))
            stok = int(input("Masukkan stok : "))
        except:
            print('\nMohon masukkan informasi yang sesuai.')
        else:    
            if (nama!="" and kategori!="" and tahun_rilis>=0 and harga>=0 and stok > 0):
                valid = True
            else:
                print("\nMohon masukkan semua informasi mengenai game dengan benar agar dapat disimpan BNMO.")

    #========== ID GAME BARU=============
    idn = ''
    id = getLength(gameArray)+1
    if (id<10):
        idn = "GAME00"+str(id)
    elif (id<100 and id>=10):
        idn = "GAME0"+str(id)
    else:
        idn = "GAME"+str(id)
    #================MENAMBAHKAN DATA GAME BARU KE ARRAY==============
    baru = [idn,nama,kategori,tahun_rilis,harga,stok]
    # temp = [0 for i in range (getLength(gameArray)+1)]
    # for i in range (getLength(gameArray)):
    #     temp[i] = gameArray[i]
    # temp[getLength(gameArray)] = baru
    # gameArray = temp

    gameArray = append_array(gameArray, baru)
    #sukses ditambahkan
    print("Selamat! Berhasil menambahkan game ",nama,".")
    return gameArray

#f05
def ubah_game(gameArray : list) -> list:
    #==============MENCARI GAME DENGAN ID GAME================
    valid_id = False
    n = 0 #deklarasi elemen
    while (not valid_id):
        idn = input("Masukkan ID game :")
        for i in range (getLength(gameArray)):
            if (idn==gameArray[i][0]):  #id berada di urutan 1  pada array game
                valid_id = True
                n = i
        if (not valid_id):
            print("ID GAME tidak terdaftar. Ulangi!")
            
    #========UBAH DATA GAME BARU===========================
    nama = input("Masukkan nama game : ")
    if (nama != ""):
        gameArray[n][1] = nama
    kategori = input("Masukkan kategori : ")
    if (kategori != ""):
        gameArray[n][2] = kategori
    tahun_rilis = input("Masukkan tahun rilis : ")
    if (tahun_rilis != ""):
        gameArray[n][3] = tahun_rilis
    harga = input("Masukkan harga: ")
    if (harga != ""):
        gameArray[n][4] = harga
    print(gameArray[n])
    #perintah sukses
    print("Selamat! Berhasil mengubah game ", gameArray[n][1],".")

    return gameArray

#f14
def help():
    printWarning('HELP MESSAGE', 100)
    print(' 1. register - untuk melakukan registrasi user baru')
    print(' 2. tambah_game_toko - untuk menambahkan game ke toko')
    print(' 3. ubah_game_toko - untuk mengubah informasi game yang ada di toko')
    print(' 4. ubah_stok_game_toko - untuk mengubah stok game yang ada di toko')
    print(' 5. list_game_toko - untuk mendaftar semua game yang ada di toko')
    print(' 6. beli_game - untuk membeli game yang ada di toko')
    print(' 7. lihat_game_toko - untuk mendaftar game yang ada di toko')
    print(' 8. cari_game_dimiliki - untuk mencari game yang sudah dimiliki')
    print(' 9. cari_game_toko - untuk mencari game yang ada di toko')
    print('10. top_up - untuk melakukan top up saldo')
    print('11. riwayat_pembelian - untuk melihat riwayat pembelian')
    print('12. help - untuk menampilkan menu bantuan ini')
    print('13. save - untuk melakukan penyimpanan data')
    print('14. exit - untuk keluar dari aplikasi')

#f15
def Load(folderArg : str) -> tuple[list, list, list, list]:
    userArr = read_csv(folderArg, 'user')
    gameArr = read_csv(folderArg, 'game')
    riwayatArr = read_csv(folderArg, 'riwayat')
    kepemilikanArr = read_csv(folderArg, 'kepemilikan')
    
    printWarning('Data from ' + folderArg + ' loaded successfully.')

    return (userArr, gameArr, riwayatArr, kepemilikanArr) # tuple, be careful

#f16
def Save(folderArg : str, userArray : list, gameArray : list, riwayatArray : list, kepemilikanArray : list):
    #folderArg = './'+ folderArg +'/' # is alr made ./{}/
    
    if folderExist(folderArg):
        save_csv(folderArg, 'user', userArray)
        save_csv(folderArg, 'game', gameArray)
        save_csv(folderArg, 'riwayat', riwayatArray)
        save_csv(folderArg, 'kepemilikan', kepemilikanArray)
    else: #folder doesnt exist
        createFolder(folderArg)
        save_csv(folderArg, 'user', userArray)
        save_csv(folderArg, 'game', gameArray)
        save_csv(folderArg, 'riwayat', riwayatArray)
        save_csv(folderArg, 'kepemilikan', kepemilikanArray)

#f17
def exit(folderPath : str, userArray : list, gameArray : list, riwayatArray : list, kepemilikanArray : list):
    # local function
    def isYes(answer : str) :
        if answer == 'y' or answer == 'Y':
            return True
        return False

    def isNo(answer : str) :
        if answer == 'n' or answer == 'N':
            return True
        return False
    
    inputDone = False
    while not inputDone:
        try:
            ans = input('Mau save? (y/n) ')
        except:
            pass
        else:
            if isYes(ans) or isNo(ans):
                inputDone = True

    if isYes(ans):
        Save(folderPath, userArray, gameArray, riwayatArray, kepemilikanArray)

    