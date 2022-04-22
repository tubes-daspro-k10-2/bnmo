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
    baru = [0,idn,nama,kategori,tahun_rilis,harga,stok]
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
            if (idn==gameArray[i][1]):  #id berada di urutan 1  pada array game
                valid_id = True
                n = i
        if (not valid_id):
            print("ID GAME tidak terdaftar. Ulangi!")
            
    #========UBAH DATA GAME BARU===========================
    nama = input("Masukkan nama game : ")
    if (nama != ""):
        gameArray[n][2] = nama
    kategori = input("Masukkan kategori : ")
    if (kategori != ""):
        gameArray[n][3] = kategori
    tahun_rilis = input("Masukkan tahun rilis : ")
    if (tahun_rilis != ""):
        gameArray[n][4] = tahun_rilis
    harga = input("Masukkan harga: ")
    if (harga != ""):
        gameArray[n][5] = harga
    print(gameArray[n])
    #perintah sukses
    print("Selamat! Berhasil mengubah game ", gameArray[n][2],".")

    return gameArray

#f06
def ubah_stok(matrix : str) :
    # Fungsi untuk F06 - Merubah stok game yang tersedia di toko

    # Menginput ID Game
    game_id = input("Masukkan ID game : ")

    # Menghapus header pada matrix
    # konten_matriks = matrix[1:]

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
        
        jumlah = int(input("Masukkan jumlah : "))

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
    sorting = input("Skema sorting : ")

    # Menghapus header pada matriks
    # konten_matriks = matrix[1:]

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
        for i in range(count) :
            print(f"{i+1}. {matrix[list_index[i]][0]} | {matrix[list_index[i]][1]} | {matrix[list_index[i]][2]} | {matrix[list_index[i]][3]} | {matrix[list_index[i]][4]} | {matrix[list_index[i]][5]}")

        return matrix

#f08
def buy_game(matrix : list[list], matrix2 : list[list], matrix3 : list[list], user_id : int) : # matriks data game, matriks data kepemilikan, matriks data user, user id
    # Fungsi untuk F08 - Membeli game
    print('leave', matrix)
    # Menginput game ID yang ingin dibeli
    game_id = input("Masukkan ID Game : ")

    # Menghapus header pada matriks
    # game_content = matrix1[1:]
    # kepemilikan_content = matrix2[1:]
    # user_content = matrix3[1:]
    game_content = [['' for i in range(7)] for j in matrix]
    kepemilikan_content = [['' for i in range(3)] for j in matrix2]
    user_content = [['' for i in range(6)] for j in matrix3]

    for i in range(getLength(matrix)):
        game_content[i][0] = (matrix[i][0])
        game_content[i][1] = (matrix[i][1])
        game_content[i][2] = (matrix[i][2])
        game_content[i][3] = (matrix[i][3])
        game_content[i][4] = int(matrix[i][4])
        game_content[i][5] = int(matrix[i][5])
        game_content[i][6] = int(matrix[i][6])

        print('GA CON\n', game_content[i])
    
    for i in range(getLength(matrix2)):
        kepemilikan_content[i] = matrix2[i]

        print('KE CON', kepemilikan_content)

    for i in range(getLength(matrix3)):
        user_content[i][0] = int(matrix3[i][0])
        user_content[i][1] = (matrix3[i][1])
        user_content[i][2] = (matrix3[i][2])
        user_content[i][3] = (matrix3[i][3])
        user_content[i][4] = (matrix3[i][4])
        user_content[i][5] = int(matrix3[i][5])
        

        print('U CON\n', user_content[i])

    # Fungsi untuk mengecek game ID dan apakah game telah dimiliki
    def id_checker(matrix, game, user): # nama matriks, game id, username
        k = 0 # variable pembantu
        found = False # variable pembantu
        while (k < getLength(matrix)) and found == False :
            if matrix == game_content :
                print(game, matrix[k][1])
                if game == matrix[k][1] : # mengecek id game
                    found = True
            elif matrix == kepemilikan_content :
                print('voila', game == matrix[k][1], int(user) == int(matrix[k][2]))
                if game == matrix[k][1] and user == int(matrix[k][2]) : # mengecek apakah game telah dimiliki
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
        print('kecheck', kepemilikan_check)
        if kepemilikan_check[1] == True :
            print("Anda sudah memiliki game tersebut")
        else :
            k = game_check[0] # indeks letak game dalam matriks
            l = user_check[0]
            if game_content[k][6] == 0 : # stok
                print("Stok Game tersbut sedang habis")
            elif game_content[k][5] > 0 : # harga
                if user_content[l][5] >= game_content[k][4] : # apakah saldo cukup untuk membeli game
                    print(f"Game {game_content[k][1]} berhasil dibeli")

                    # Mengurangi stok setelah dibeli
                    game_content[k][6] -= 1
                    user_content[l][5] -= game_content[k][5]
                    # Menambah data ke dalam matriks kepemilikan_data
                    # matrix2 = add_row(matrix2) # menambah slot baris baru
                    # matrix2[-1][0] = game_id # mengisi data pembelian
                    # matrix2[-1][1] = user_id # mengisi data pembelian

                    kepemilikan_content = append_array(kepemilikan_content, [getLength(kepemilikan_content), game_id, user_id])
                    print(kepemilikan_content)
                else :
                    print("Saldo Anda tidak cukup untuk membeli game tersebut")
            else: #free game
                print(f"Game {game_content[k][1]} berhasil dibeli")

                # Mengurangi stok setelah dibeli
                game_content[k][6] -= 1
                user_content[l][5] -= game_content[k][5]
                # Menambah data ke dalam matriks kepemilikan_data
                # matrix2 = add_row(matrix2) # menambah slot baris baru
                # matrix2[-1][0] = game_id # mengisi data pembelian
                # matrix2[-1][1] = user_id # mengisi data pembelian

                kepemilikan_content = append_array(kepemilikan_content, [getLength(kepemilikan_content), game_id, user_id])
                print(kepemilikan_content)


    return game_content, kepemilikan_content, user_content

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

    