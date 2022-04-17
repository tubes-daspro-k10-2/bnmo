#data :
#     data[0] : user.csv
#     data[1] : game.csv


import variabelGlobal as g
from variabelGlobal import len
#from load import * 

def ubah_game(data):
    #g.login = True
    #g.role = "Admin"
    game = data[1]
    if (not g.login):
        print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login".')
        return;
    else:
        if (g.role != "Admin"):
             print("\nMaaf, hanya role admin yang dapat mengirim perintah ini.")
        else:
            #==============MENCARI GAME DENGAN ID GAME================
            valid_id = False
            n = 0 #deklarasi elemen
            while (not valid_id):
                idn = input("Masukkan ID game :")
                for i in range (len(game)):
                    if (idn==game[i][0]):  #id berada di urutan 1  pada array game
                        valid_id = True
                        n = i
                if (not valid_id):
                    print("ID GAME tidak terdaftar. Ulangi!")
                    
            #========UBAH DATA GAME BARU===========================
            nama = input("Masukkan nama game : ")
            if (nama != ""):
                game[n][1] = nama
            kategori = input("Masukkan kategori : ")
            if (kategori != ""):
                game[n][2] = kategori
            tahun_rilis = input("Masukkan tahun rilis : ")
            if (tahun_rilis != ""):
                game[n][3] = tahun_rilis
            harga = input("Masukkan harga: ")
            if (harga != ""):
                game[n][4] = harga
            print(game[n])
            #perintah sukses
            print("Selamat! Berhasil mengubah game ",game[n][1],".")

#data = load("eksternal")
#ubah_game(data)
