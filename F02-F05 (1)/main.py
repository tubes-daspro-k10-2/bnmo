#ini cuma buat testing fungsi-fungsi yang udah kubuat.

import variabelGlobal as g
from load import *
from F02 import *
from F03 import *
from F04 import *
from F05 import *

print("KETIK 'help' untuk melihat panduan program")
def helpp():
    print("============COMMAND YANG TERSEDIA==========")
    print("load        : data diload agar data dapat digunakan")
    print("register    : melakukan pendaftaran user baru ")
    print("login       : login ke program")
    print("tambah_game : menambahkan sebuah game baru")
    print("ubah_game   : mengubah data sebuah game")
    print("exit        : untuh keluar dari program")
    print("===========================================")

exit_game = False
while (not exit_game):
    perintah = input(">>>")
    if (perintah == "help"):
        helpp()
    elif (perintah == "load"):
        data = load('eksternal')
        print("Data berhasil di-load")
    elif (perintah=="register"):
        register(data)
    elif (perintah=="login"):
        login(data)
    elif (perintah=="tambah_game"):
        tambah_game(data)
    elif (perintah=="ubah_game"):
        ubah_game(data)
    elif (perintah=="exit"):
        print("Terima kasih!")
        exit_game = True
        sleep()
    else:
        print("Masukan salah.")
