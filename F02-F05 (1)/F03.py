#data :
#     data[0] : user.csv
#     data[1] : game.csv

import variabelGlobal as g
from load import *

def login(data):
    if (g.login):
        print("Anda telah login")
        return;
    else:
        user=data[0]
        username = input("Masukan username: ")
        password = input("Masukan password: ")


        ada = False
        i=0
        while ((not ada) and i < len(user)):
            if (user[i][1] == username and user[i][3]==password):
                print("\nHalo ", username, "! Selamat datang di Binomo.")
                ada = True
                #update variabel global
                g.login = True
                
                g.id = user[i][0]
                g.username = user[i][1]
                g.nama = user[i][2]
                g.password = user[i][3]
                g.role = user[i][4]
                g.saldo = user[i][5]
            i += 1
        if (not ada):
            print("\nMasukan username atau password salah atau tidak ditemukan")

#data = load('eksternal')
#login(data)
#login(data)