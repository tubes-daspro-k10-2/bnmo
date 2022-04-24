from array import array
import time
from front.ui import helpText

from utils.file import append_array, read_csv, folderExist, createFolder, save_csv, getIndexByName
from utils.ui import getBoxUI, makeBoxUI, printCenter, printWarning, validIntegerInput, validStringInput
from utils.user import isUsernameValid
from utils.main import getLength

from body.function_cipher import encrypt, decrypt

from constants import emptySessionAccount, gamecsvHeader, riwayatcsvHeader, usercsvHeader, kepemilikancsvHeader

#f02
def register(userArray, nama, username, password) -> list[str, str, str, str]:
    #=====================INPUT DATA===================
    user_valid = False
    while (not user_valid):
        
        terdaftar = False
        i = 0
        while ((not terdaftar) and i < getLength(userArray)):
            if (userArray[i][getIndexByName('username', 'user')] == username):
                print("\nUsername ",username," sudah terpakai, silakan menggunakan username lain.")
                terdaftar = True
                return userArray
            i+=1
        if (not terdaftar):
            if (isUsernameValid(username)):
                user_valid = True
            else:
                print("Username hanya dapat mengandung alfabet A-Z a-z, underscore '_', strip '-', dan angka 0-9") 
                return userArray
            
    
    #======================TAMBAHKAN DATA BARU===================
    idn = getLength(userArray)

    encryptedPassword = encrypt(password) ## cipher

    baru = [str(idn+1), username, nama, encryptedPassword, "user", 0] #id,username,name,password,role,saldo

    userArray = append_array(userArray, baru)

    #sukses didaftarkan
    print("\nUsername ",username,' telah berhasil register ke dalam "Binomo"')

    return userArray

#f03
def login(userArray : list, username : str, password : str) -> list[str, str, str, str]:
    encryptedPassword = encrypt(password)
    
    ada = False
    i=0
    while ((not ada) and i < getLength(userArray)):
        if (userArray[i][getIndexByName('username', 'user')] == username and userArray[i][getIndexByName('password', 'user')]==encryptedPassword):
            printCenter("Halo " + str(username) + "! Selamat datang di Binomo.", )
            ada = True
            
            # tangkep nilainya di main
            return userArray[i][getIndexByName('username', 'user')], userArray[i][getIndexByName('name', 'user')], userArray[i][getIndexByName('saldo', 'user')], userArray[i][getIndexByName('role', 'user')], userArray[i][getIndexByName('id', 'user')] #username, name, saldo, role       
        i += 1

    print("\nMasukan username atau password salah atau tidak ditemukan\n")

    return emptySessionAccount

#f04
def tambah_game(gameArray : list) -> list:

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
    baru = [idn, nama, kategori, tahun_rilis, harga, stok]

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
        idn = validStringInput("Masukkan ID game :")
        for i in range (getLength(gameArray)):
            if (idn==gameArray[i][getIndexByName('id', 'game')]):  #id berada di urutan 1  pada array game
                valid_id = True
                n = i
        if (not valid_id):
            print("ID GAME tidak terdaftar. Ulangi!")
            
    #========UBAH DATA GAME BARU===========================
    nama = validStringInput("Masukkan nama game : ", [';'])
    if (nama != ""):
        gameArray[n][getIndexByName('nama', 'game')] = nama
    kategori = validStringInput("Masukkan kategori : ", [';'])
    if (kategori != ""):
        gameArray[n][getIndexByName('kategori', 'game')] = kategori
    tahun_rilis = validIntegerInput("Masukkan tahun rilis : ", lowerLimit=0)
    if (tahun_rilis != ""):
        gameArray[n][getIndexByName('tahun_rilis', 'game')] = tahun_rilis
    harga = validIntegerInput("Masukkan harga: ", lowerLimit=0)
    if (harga != ""):
        gameArray[n][getIndexByName('harga', 'game')] = harga
    
    #perintah sukses
    print("Selamat! Berhasil mengubah game ", gameArray[n][getIndexByName('nama', 'game')],".")

    return gameArray

#f06
def ubah_stok(matrix : str) :
    # Fungsi untuk F06 - Merubah stok game yang tersedia di toko

    # Menginput ID Game
    game_id = validStringInput("Masukkan ID game : ")

    # Menghapus header pada matrix
    # konten_matriks = matrix[1:] # data alr no header

    # Menghitung banyak baris pada matrix
    count = getLength(matrix)

    # Mengecek apakah ada game yang sesuai dengan game_id yang telah diinput
    j = 0 # index
    found = False # variabel pembantu
    while (j < count) and found == False :
        if matrix[j][0] == game_id :
            found = True
        j += 1

    # Mengubah stok game
    if found == True :
        jumlah = validIntegerInput("Masukkan jumlah : ")

        if jumlah > 0 :
            n = "ditambahkan" # variable pembantu
        else :
            n = "dikurangi" # variabel pembantu
        
        matrix[j-1][5] = int(matrix[j-1][5])

        if (matrix[j-1][5] + jumlah) >= 0 :
            print(f"Stok game {matrix[j-1][1]} berhasil " + n + f". Stok sekarang : {matrix[j-1][5] + jumlah}")
            matrix[j-1][5] += jumlah
        else :
            print(f"Stok game {matrix[j-1][1]} gagal " + n + f". Stok sekarang : {matrix[j-1][5]}")
    else :
        print("Tidak ada game dengan ID tersebut!")

    return matrix

#f07
def list_game_toko(matrix) :
    # Fungsi untuk F07 - Menampilkan list game pada toko sesuai urutan

    # Menginput skema sorting
    sorting = validStringInput("Skema sorting : ")

    # Menghitung banyak baris pada konten_matrix
    count = getLength(matrix)

    # Membuat matrix tambahan untuk menyimpan index yang telah diurutkan beserta variabel yang ingin diurutkan
    list_data = [[0 for j in range(count)] for i in range(2)]

    # Menginput data yang akan disorting beserta index ke list_data
    valid = True
    if sorting == "tahun+" or sorting == "tahun-" :
        for i in range(count) :
            list_data[0][i] = int(matrix[i][3])
            list_data[1][i] = i
    elif sorting == "harga+" or sorting == "harga-" :
        for i in range(count) :
            list_data[0][i] = int(matrix[i][4])
            list_data[1][i] = i
    elif sorting == "" :
        for i in range(count) :
            list_data[0][i] = int(matrix[i][0][4:])
            list_data[1][i] = i
    else :
        print("Skema sorting tidak valid!")
        valid = False
    
    # Mengurutkan data menggunakan selection sort
    if valid == True : # Jika skema telah valid
        for i in range(count) :
            Imax = i
            if sorting == "" :
                for j in range(i+1, count) :
                    if list_data[0][Imax] > list_data[0][j] :
                        Imax = j
            elif sorting[-1] == "-" :
                for j in range(i+1, count) :
                    if list_data[0][Imax] < list_data[0][j] :
                        Imax = j
            else :
                for j in range(i+1, count) :
                    if list_data[0][Imax] > list_data[0][j] :
                        Imax = j
            Temp = [list_data[0][Imax], list_data[1][Imax]]
            list_data[0][Imax] = list_data[0][i]
            list_data[1][Imax] = list_data[1][i]
            list_data[0][i] = Temp[0]
            list_data[1][i] = Temp[1]
        
        # Menuliskan index yang telah diurutkan sesuai skema
        list_index = [0 for i in range(count)]
        for i in range(count) :
            list_index[i] = list_data[1][i]

        # Mengeprint list game
        contentToPrint = []
        for i in range(count) :
            contentToPrint += [matrix[list_index[i]]]
        makeBoxUI(contentToPrint, ['Game ID', 'Nama Game', 'Kategori', 'Tahun Rilis', 'Harga', 'Stok'])
        
        return

#f08
def buy_game(matrix : list[list], matrix2 : list[list], matrix3 : list[list], matrix4 : list[list], user_id : int) : # matriks data game, matriks data kepemilikan, matriks data user, user id
    # Fungsi untuk F08 - Membeli game

    # Menginput game ID yang ingin dibeli
    game_id = validStringInput("Masukkan ID Game : ")

    
    # Menghapus header pada matriks # data alr no header
    # game_content = matrix1[1:]
    # kepemilikan_content = matrix2[1:]
    # user_content = matrix3[1:]

    # empty array problem
    game_content = [['' for i in range(getLength(gamecsvHeader))] for j in matrix]
    kepemilikan_content = [['' for i in range(getLength(kepemilikancsvHeader))] for j in matrix2]
    user_content = [['' for i in range(getLength(usercsvHeader))] for j in matrix3]
    riwayat_content = [['' for i in range(getLength(riwayatcsvHeader))] for j in matrix4]

    # TAHUN BELI
    tahun_beli = time.localtime(time.time()).tm_year

    for i in range(getLength(matrix)):#CHANGE
        for j in range(getLength(matrix[i])):
            game_content[i][j] = matrix[i][j]
    
    for i in range(getLength(matrix2)):#CHANGE
        kepemilikan_content[i] = matrix2[i]

    for i in range(getLength(matrix3)):#CHANGE
        for j in range(getLength(user_content[i])):
            user_content[i][j] = matrix3[i][j]
    
    for i in range(getLength(matrix4)):
        for j in range(getLength(riwayat_content[i])):
            riwayat_content[i][j] = matrix4[i][j]

    # Fungsi untuk mengecek game ID dan apakah game telah dimiliki
    def id_checker(matrix, game, user): # nama matriks, game id, username
        k = 0 # variable pembantu
        found = False # variable pembantu
        while (k < getLength(matrix)) and found == False :
            if matrix == game_content :
                if game == matrix[k][0] : # mengecek id game #CHANGE
                    found = True
            elif matrix == kepemilikan_content :
                if game == matrix[k][getIndexByName('game_id', 'kepemilikan')] and user == matrix[k][getIndexByName('user_id', 'kepemilikan')] : # mengecek apakah game telah dimiliki
                    found = True
            elif matrix == user_content :
                if matrix[k][0] == user :
                    found = True
            k += 1
        result = [(k-1), found] # index dan found
        return result
    
    # Mengecek game ID
    game_check = id_checker(game_content, game_id, user_id)
    # Mengecek kepemilikan game
    kepemilikan_check = id_checker(kepemilikan_content, game_id, user_id)
    # Mengecek user data
    user_check = id_checker(user_content, game_id, user_id)
    

    # Membeli game
    if game_check[1] == False :
        print("Tidak ada game dengan ID tersebut")
    else :
        # print('kecheck', kepemilikan_check)
        if kepemilikan_check[1] == True :
            print("Anda sudah memiliki game tersebut")
        else :
            k = game_check[0] # indeks letak game dalam matriks
            l = user_check[0]
            if game_content[k][getIndexByName('stok', 'game')] == 0 : # stok
                print("Stok Game tersbut sedang habis")
            elif game_content[k][getIndexByName('harga', 'game')] > 0 : # harga
                if user_content[l][getIndexByName('saldo', 'user')] >= game_content[k][getIndexByName('harga', 'game')] : # apakah saldo cukup untuk membeli game
                    print(f"Game {game_content[k][1]} berhasil dibeli")

                    # Mengurangi stok setelah dibeli
                    game_content[k][getIndexByName('stok', 'game')] -= 1
                    user_content[l][getIndexByName('saldo', 'user')] -= game_content[k][getIndexByName('harga', 'game')]
                    # Menambah data ke dalam matriks kepemilikan_data  # append replaced
                    # matrix2 = add_row(matrix2) # menambah slot baris baru
                    # matrix2[-1][0] = game_id # mengisi data pembelian
                    # matrix2[-1][1] = user_id # mengisi data pembelian

                    kepemilikan_content = append_array(kepemilikan_content, [game_id, user_id])
                    riwayat_content = append_array(riwayat_content, [game_id, game_content[k][getIndexByName('nama', 'game')], game_content[k][getIndexByName('harga', 'game')], user_id, tahun_beli])
                else :
                    print("Saldo Anda tidak cukup untuk membeli game tersebut")
            else: #free game
                print(f"Game {game_content[k][1]} berhasil dibeli")

                # Mengurangi stok setelah dibeli
                game_content[k][getIndexByName('stok', 'game')] -= 1
                user_content[l][getIndexByName('saldo', 'user')] -= game_content[k][getIndexByName('harga', 'game')]
                # Menambah data ke dalam matriks kepemilikan_data # append replaced
                # matrix2 = add_row(matrix2) # menambah slot baris baru
                # matrix2[-1][0] = game_id # mengisi data pembelian
                # matrix2[-1][1] = user_id # mengisi data pembelian

                kepemilikan_content = append_array(kepemilikan_content, [game_id, user_id])
                riwayat_content = append_array(riwayat_content, [game_id, game_content[k][getIndexByName('nama', 'game')], game_content[k][getIndexByName('harga', 'game')], user_id, tahun_beli])

    return game_content, kepemilikan_content, user_content, riwayat_content

#f09
def list_game(game_content, kepemilikan_content, user_id) :

    game_count = getLength(game_content)
    user_count = getLength(kepemilikan_content)

    j = 1

    contentToPrint = []
    for i in range(user_count) :
        if kepemilikan_content[i][getIndexByName('user_id', 'kepemilikan')] == user_id :
            k = 0
            found = 0
            while (k < game_count) and found == False :
                if game_content[k][getIndexByName('id', 'game')] == kepemilikan_content[i][getIndexByName('game_id', 'kepemilikan')] :
                    found = True
                else :
                    k += 1
            
            contentToPrint += [[game_content[k][0], game_content[k][1], game_content[k][2], game_content[k][3], game_content[k][4]]]
            #print(f"{j}. {game_content[k][0]} | {game_content[k][1]} | {game_content[k][2]} | {game_content[k][3]} | {game_content[k][4]}")
            # 
            
            j += 1
    
    makeBoxUI(contentToPrint, ['ID', 'Nama game', 'Kategori', 'Tahun Rilis', 'Harga'])

    if j == 1 :
        print("Maaf, kamu belum memiliki game. Ketik perintah buy_game untuk membeli")
        


#f10
def search_my_game(listgame,listkepemilikan,userid):
    idgame = input('Masukkan ID Game: ')
    tahunrilis = input('Masukkan Tahun Rilis Game: ')
    
    ada = False
    no = 1

    contentToPrint = []

    # apakah kepemilikan kosong
    def isKepemilikanKosong(listkepemilikan,userid):
        count = 0
        for i in range(getLength(listkepemilikan)):
            for j in range(2):
                if listkepemilikan[i][1] == userid :
                    count += 1
    
        return not count > 0
    
    if not isKepemilikanKosong(listkepemilikan,userid):
        if (idgame != '') :
            for j in range(getLength(listkepemilikan)):
                if (idgame == listkepemilikan[j][0] and userid == listkepemilikan[j][1]):
                    for i in range(getLength(listgame)):
                        if (tahunrilis != ''):
                            if (idgame == listgame[i][0] and tahunrilis == str(listgame[i][3])):
                               # print(f"{no}. {listgame[i][0]} | {listgame[i][1]} | {listgame[i][4]} | {listgame[i][2]} | {listgame[i][3]}")
                                contentToPrint += [[listgame[i][0], listgame[i][1], listgame[i][4], listgame[i][2], listgame[i][3]]]
                                ada = True
                                break
                        else:
                            if (idgame == listgame[i][0]):
                                # print(f"{no}. {listgame[i][0]} | {listgame[i][1]} | {listgame[i][4]} | {listgame[i][2]} | {listgame[i][3]}")
                                contentToPrint += [[listgame[i][0], listgame[i][1], listgame[i][4], listgame[i][2], listgame[i][3]]]
                                ada = True
                                break
        else:
            for j in range(getLength(listkepemilikan)):
                if (userid == listkepemilikan[j][1]):
                    idgame = listkepemilikan[j][0]
                    for i in range(getLength(listgame)):
                        if (tahunrilis != ''):
                            if (idgame == listgame[i][0] and tahunrilis == str(listgame[i][3])):
                                # print(f"{no}. {listgame[i][0]} | {listgame[i][1]} | {listgame[i][4]} | {listgame[i][2]} | {listgame[i][3]}")
                                contentToPrint += [[listgame[i][0], listgame[i][1], listgame[i][4], listgame[i][2], listgame[i][3]]]
                                ada = True
                                no += 1
                        else:
                            if (idgame == listgame[i][0]):
                                # print(f"{no}. {listgame[i][0]} | {listgame[i][1]} | {listgame[i][4]} | {listgame[i][2]} | {listgame[i][3]}")
                                contentToPrint += [[listgame[i][0], listgame[i][1], listgame[i][4], listgame[i][2], listgame[i][3]]]
                                ada = True
                                no += 1

        makeBoxUI(contentToPrint, ['ID Game', 'Nama Game', 'Harga', 'Kategori', 'Tahun RIlis'])

        if not ada:
            print('Tidak ada game pada inventory-mu yang memenuhi kriteria.')
        return

    else:
        print('Tidak ada game pada inventory-mu yang memenuhi kriteria.')
        return

#f11
def search_game_at_store(arrayGame):
    id = input('Masukkan Game ID: ')
    game = input('Masukkan Nama Game: ')
    harga = input('Masukkan Harga Game: ')
    kategori = input('Masukkan Kategori Game: ')
    tahunrilis = input('Masukkan Tahun Rilis Game: ')
    
    contentToPrint = []

    x = 0
    for i in range (getLength(arrayGame)):
        if ((id == "") or (id == arrayGame[i][0])) and ((game == "") or (game == arrayGame[i][1])) and ((harga == "") or (harga == str(arrayGame[i][4]))) and ((kategori == "") or (kategori == arrayGame[i][2])) and ((tahunrilis == "") or (tahunrilis == str(arrayGame[i][3]))) :
            x = x + 1
            # print(f"{x}. {arrayGame[i][0]} | {arrayGame[i][1]} | {arrayGame[i][4]} | {arrayGame[i][2]} | {arrayGame[i][3]} | {arrayGame[i][5]}")
            contentToPrint += [[arrayGame[i][0], arrayGame[i][1], arrayGame[i][4], arrayGame[i][2], arrayGame[i][3]]]
                   
    if x == 0 :
        print('Tidak ada game pada toko yang memenuhi kriteria.')
    
    makeBoxUI(contentToPrint, ['Game ID', 'Nama Game', 'Harga', 'Kategori', 'Tahun Rilis'])

#f12
def topup(matriksUser):
    username = input('Masukkan username: ')
    saldo = int(input('Masukkan saldo: '))
    
    for i in range(getLength(matriksUser)):
        if username == matriksUser[i][getIndexByName('username', 'user')] :
            saldoawal = int(matriksUser[i][getIndexByName('saldo', 'user')])
            if (saldoawal + saldo) >= 0 :
                saldoawal += saldo
                matriksUser[i][getIndexByName('saldo', 'user')] = str(saldoawal)
                print(f"Top up berhasil. Saldo {matriksUser[i][getIndexByName('username', 'user')]} berubah menjadi {matriksUser[i][getIndexByName('saldo', 'user')]}.")
                return matriksUser
            else :
                print('Masukan tidak valid.')
                return matriksUser
    print(f'Username "{username}" tidak ditemukan.')

    return matriksUser

#f13
def riwayat(matriks,userid):
    contentToPrint = []

    adaRiwayat = False
    no = 1
    for i in range(getLength(matriks)):
        if userid == matriks[i][getIndexByName('user_id', 'riwayat')]:
            # print(f"{no}. {matriks[i][0]} | {matriks[i][1]} | {matriks[i][2]} | {matriks[i][4]}")
            contentToPrint += [[matriks[i][0], matriks[i][1], str(matriks[i][2]), str(matriks[i][4])]]
            adaRiwayat = True
            no += 1
    
    if not adaRiwayat:
        print('Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.')
    else:
        print('Riwayat pembelian anda :')
        makeBoxUI(contentToPrint, ['Game ID', 'Nama Game', 'Harga', 'Tahun Beli'])
        
    return

#f14
def help(sessionAccount : list):
    printWarning('HELP MESSAGE', 100)
    helpText(sessionAccount)

#f15
def Load(folderArg : str) -> tuple[list, list, list, list]:
    userArr = read_csv(folderArg, 'user')
    gameArr = read_csv(folderArg, 'game')
    riwayatArr = read_csv(folderArg, 'riwayat')
    kepemilikanArr = read_csv(folderArg, 'kepemilikan')
    
    printWarning('Data from ' + folderArg + ' loaded successfully.')

    for i in range(getLength(userArr)):
        for j in range(getLength(userArr[i])):
            if j == getIndexByName('saldo', 'user'):
                userArr[i][j] = int(userArr[i][j])

    for i in range(getLength(gameArr)):
        for j in range(getLength(gameArr[i])):
            if j == getIndexByName('tahun_rilis', 'game') or j == getIndexByName('harga', 'game') or j == getIndexByName('stok', 'game'):
                gameArr[i][j] = int(gameArr[i][j])
    
    for i in range(getLength(riwayatArr)):
        for j in range(getLength(riwayatArr[i])):
            if j == getIndexByName('harga', 'riwayat') or j == getIndexByName('tahun_beli', 'riwayat'):
                riwayatArr[i][j] = int(riwayatArr[i][j])
    

    return (userArr, gameArr, riwayatArr, kepemilikanArr) # tuple, be careful

#f16
def Save(folderArg : str, userArray : list, gameArray : list, riwayatArray : list, kepemilikanArray : list):
    #folderArg = './'+ folderArg +'/' # is alr made ./{}/
    newFolderArg = str(input('Masukkan nama folder penyimpanan : '))

    if newFolderArg == '':
        newFolderArg = folderArg
    else:
        newFolderArg = './' + newFolderArg + '/'

    if folderExist(newFolderArg):
        save_csv(newFolderArg, 'user', userArray)
        save_csv(newFolderArg, 'game', gameArray)
        save_csv(newFolderArg, 'riwayat', riwayatArray)
        save_csv(newFolderArg, 'kepemilikan', kepemilikanArray)
    else: #folder doesnt exist
        createFolder(newFolderArg)
        save_csv(newFolderArg, 'user', userArray)
        save_csv(newFolderArg, 'game', gameArray)
        save_csv(newFolderArg, 'riwayat', riwayatArray)
        save_csv(newFolderArg, 'kepemilikan', kepemilikanArray)

    print()
    print('Saving ...')
    time.sleep(2)
    print('Data telah disimpan dalam folder :', newFolderArg)

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
        input()

    