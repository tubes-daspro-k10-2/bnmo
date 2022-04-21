from utils.file import append_array, read_csv, folderExist, createFolder, save_csv
from utils.ui import printWarning
from utils.user import isUsernameValid
from utils.main import getLength

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
    baru = [str(idn),username,nama,password,"user",0] #id,username,name,password,role,saldo
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
    ada = False
    i=0
    while ((not ada) and i < getLength(userArray)):
        if (userArray[i][1] == username and userArray[i][3]==password):
            print("\nHalo ", username, "! Selamat datang di Binomo.")
            ada = True
            
            # tangkep nilainya di main
            return userArray[i][1], userArray[i][2], userArray[i][5], userArray[i][4] #username, name, saldo, role       
        i += 1

    print("\nMasukan username atau password salah atau tidak ditemukan")

    return emptySessionAccount

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
def Save(folderArg : str, userArray : list):
    #folderArg = './'+ folderArg +'/' # is alr made ./{}/
    
    if folderExist(folderArg):
        save_csv(folderArg, 'user', userArray)
    else: #folder doesnt exist
        createFolder(folderArg)

#f17
def exit(folderPath : str, userArray : list):
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
        Save(folderPath, userArray)

    