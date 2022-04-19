from side_function import * # fungsi yang diimport : length, add_row

def convert_csv(csv_file_name) :
    # Fungsi untuk merubah data didalam CSV menjadi bentuk matriks

    # Membuka dan membaca file CSV
    with open(csv_file_name, "r") as file_csv :
        raw_data = file_csv.readlines()

    count_column = 0 # variabel banyak kolom matriks
    count_row = 0 # variabel banyak baris matriks

    # Mencari banyak kolom
    for i in range(length(raw_data[0])):
        if raw_data[0][i] == ";" : # menambah jumlah kolom ketika terdapat ";"
            count_column += 1
    count_column += 1

    # Mencari banyak baris
    for i in raw_data:
        count_row += 1

    # Membuat matriks kosong untuk menyimpan data
    main_data = [["" for j in range(count_column)] for i in range(count_row)]

    # Menginput data dalam matriks
    k = 0 # index
    found = False # variabel untuk menghindari "\n" diinput ke dalam matriks
    for i in range(count_row) :
        for j in range(length(raw_data[i])) :
            if found == False :
                if raw_data[i][j] != ";" : # Split data setiap terdapat ";"
                    if ord(raw_data[i][j]) == 10 :
                        found == True # merubah nilai found jika sudah berada di "\"
                    else :
                        main_data[i][k] += raw_data[i][j]
                else :
                    k += 1
        k = 0 # mereset nilai
        found = False # mereset nilai


    # Mengubah tipe data ke integer jika ada
    found = False
    for i in range(count_row) :
        for j in range(count_column) :
            while (k < length(main_data[i][j])) and found == False :
                if ((ord(main_data[i][j][k])) < 48) or ((ord(main_data[i][j][k])) > 57) : # Mengecek apakah terdapat character
                    found = True
                k += 1
            if found == False :
                main_data[i][j] = int(main_data[i][j]) # merubah type jika hanya terdapat angka didalamnya
            found = False # mereset nilai
            k = 0 # mereset nilai
    
    return main_data # mengembalikan matriks yang telah terisi data

def ubah_stok(matrix) :
    # Fungsi untuk F06 - Merubah stok game yang tersedia di toko

    # Menginput ID Game
    game_id = input("Masukkan ID game : ")

    # Menghapus header pada matrix
    konten_matriks = matrix[1:]

    # Menghitung banyak baris pada matrix
    count = length(konten_matriks)

    # Mengecek apakah ada game yang sesuai dengan game_id yang telah diinput
    j = 0 # index
    found = False # variabel pembantu
    while (j < count) and found == False :
        if konten_matriks[j][0] == game_id :
            found = True
        j += 1

    # Mengubah stok game
    if found == True :
        jumlah = int(input("Masukkan jumlah : "))

        if jumlah > 0 :
            n = "ditambahkan" # variable pembantu
        else :
            n = "dikurangi" # variabel pembantu
        
        if (konten_matriks[j-1][5] + jumlah) >= 0 :
            print(f"Stok game {konten_matriks[j-1][1]} berhasil " + n + f". Stok sekarang : {konten_matriks[j-1][5] + jumlah}")
            konten_matriks[j-1][5] += jumlah
        else :
            print(f"Stok game {konten_matriks[j-1][1]} gagal " + n + f". Stok sekarang : {konten_matriks[j-1][5]}")
    else :
        print("Tidak ada game dengan ID tersebut!")

def list_game_toko(matrix) :
    # Fungsi untuk F07 - Menampilkan list game pada toko sesuai urutan

    # Menginput skema sorting
    sorting = input("Skema sorting : ")

    # Menghapus header pada matriks
    konten_matriks = matrix[1:]

    # Menghitung banyak baris pada konten_matrix
    count = length(konten_matriks)

    # Membuat matrix tambahan untuk menyimpan index yang telah diurutkan beserta variabel yang ingin diurutkan
    list_data = [[0 for j in range(count)] for i in range(2)]

    # Menginput data yang akan disorting beserta index ke list_data
    valid = True
    if sorting == "tahun+" or sorting == "tahun-" :
        for i in range(count) :
            list_data[0][i] = konten_matriks[i][3]
            list_data[1][i] = i
    elif sorting == "harga+" or sorting == "harga-" :
        for i in range(count) :
            list_data[0][i] = konten_matriks[i][4]
            list_data[1][i] = i
    elif sorting == "" :
        for i in range(count) :
            list_data[0][i] = int(konten_matriks[i][0][4:])
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
            print(f"{i+1}. {konten_matriks[list_index[i]][0]} | {konten_matriks[list_index[i]][1]} | {konten_matriks[list_index[i]][2]} | {konten_matriks[list_index[i]][3]} | {konten_matriks[list_index[i]][4]} | {konten_matriks[list_index[i]][5]}")

def buy_game(matrix1, matrix2, matrix3, user_id) : # matriks data game, matriks data kepemilikan, matriks data user, user id
    # Fungsi untuk F08 - Membeli game

    # Menginput game ID yang ingin dibeli
    game_id = input("Masukkan ID Game : ")

    # Menghapus header pada matriks
    game_content = matrix1[1:]
    kepemilikan_content = matrix2[1:]
    user_content = matrix3[1:]

    # Fungsi untuk mengecek game ID dan apakah game telah dimiliki
    def id_checker(matrix, game, user): # nama matriks, game id, username
        k = 0 # variable pembantu
        found = False # variable pembantu
        while (k < length(matrix)) and found == False :
            if matrix == game_content :
                if game == matrix[k][0] : # mengecek id game
                    found = True
            elif matrix == kepemilikan_content :
                if game == matrix[k][0] and user == matrix[k][1] : # mengecek apakah game telah dimiliki
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
        if kepemilikan_check[1] == True :
            print("Anda sudah memiliki game tersebut")
        else :
            k = game_check[0] # indeks letak game dalam matriks
            l = user_check[0]
            if game_content[k][5] == 0 :
                print("Stok Game tersbut sedang habis")
            elif game_content[k][5] > 0 :
                if user_content[l][5] >= game_content[k][4] : # apakah saldo cukup untuk membeli game
                    print(f"Game {game_content[k][1]} berhasil dibeli")

                    # Mengurangi stok setelah dibeli
                    game_content[k][5] -= 1
                    user_content[l][5] -= game_content[k][4]
                    # Menambah data ke dalam matriks kepemilikan_data
                    matrix2 = add_row(matrix2) # menambah slot baris baru
                    matrix2[-1][0] = game_id # mengisi data pembelian
                    matrix2[-1][1] = user_id # mengisi data pembelian
                else :
                    print("Saldo Anda tidak cukup untuk membeli game tersebut")

    return matrix2                

def list_game(matrix1, matrix2, user_id) :

    game_content = matrix1[1:]
    user_content = matrix2[1:]

    game_count = length(game_content)
    user_count = length(user_content)

    j = 1

    for i in range(user_count) :
        if user_content[i][1] == user_id :
            k = 0
            found = 0
            while (k < game_count) and found == False :
                if game_content[k][0] == user_content[i][0] :
                    found = True
                else :
                    k += 1
            print(f"{j}. {game_content[k][0]} | {game_content[k][1]} | {game_content[k][2]} | {game_content[k][3]} | {game_content[k][4]}")
            j += 1
    
    if j == 1 :
        print("Maaf, kamu belum memiliki game. Ketik perintah buy_game untuk membeli")
