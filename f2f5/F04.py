#data :
#     data[0] : user.csv
#     data[1] : game.csv


import variabelGlobal as g
from variabelGlobal import len

def tambah_game(data):
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
            valid = False
            while (not valid):
            #========INPUT DATA GAME BARU===========================
                nama = input("Masukkan nama game : ")
                kategori = input("Masukkan kategori : ")
                tahun_rilis = input("Masukkan tahun rilis : ")
                harga = input("Masukkan harga: ")
                stok = input("Masukkan stok : ")
                if (nama!="" and kategori!="" and tahun_rilis!="" and harga!="" and stok!=""):
                    valid = True
                else:
                    print("\nMohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
            #========== ID GAME BARU=============
            idn = ''
            if (len(game)<10):
                idn = "GAME00"+str(len(game))
            elif (len(game)<100 and len(game)>=10):
                idn = "GAME0"+str(len(game))
            else:
                idn = "GAME"+str(len(game))
            #================MENAMBAHKAN DATA GAME BARU KE ARRAY==============
            baru = [idn,nama,kategori,tahun_rilis,harga,stok]
            temp = [0 for i in range (len(game)+1)]
            for i in range (len(game)):
                temp[i] = game[i]
            temp[len(game)] = baru
            game = temp
            #sukses ditambahkan
            print("Selamat! Berhasil menambahkan game ",nama,".")

#data = load("eksternal")
#tambah_game(data)