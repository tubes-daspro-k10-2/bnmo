#data :
#     data[0] : user.csv
#     data[1] : game.csv

import variabelGlobal as g
from variabelGlobal import len

def valid_user(s):
    for i in s:
        if (i=='-' or i=='_' or 'a'<=i<='z' or 'A'<=i<='Z' or '0'<=i<='9'):
            continue
        else:
            return False
            break
    return True
    

def register(data):
    user = data[0]
    #g.login = True
    #g.role = "Admin"
    if (not g.login):
        print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login".')
        return;
    else:
        if (g.role != "Admin"):
            print("\nMaaf, hanya role admin yang dapat mengirim perintah ini.")
        else:
            #=====================INPUT DATA===================
            user_valid = False
            while (not user_valid):
                nama = input("Masukan nama: ")
                username = input("Masukan username: ")
                password = input("Masukan password: ")
                
                terdaftar = False
                i = 0
                while ((not terdaftar) and i < len(user)):
                    if (user[i][1] == username):
                        print("\nUsername ",username," sudah terpakai, silakan menggunakan username lain.")
                        terdaftar = True
                    i+=1
                if (not terdaftar):
                    if (valid_user(username)):
                        user_valid = True
                    else:
                        print("Username hanya dapat mengandung alfabet A-Z a-z,unserscore'_',strip'-',dan angka 0-9") 
                    
            
            #======================TAMBAHKAN DATA BARU===================
            idn = len(user)
            baru = [str(idn),username,nama,password,"User",0]
            temp = [0 for i in range (len(user)+1)]
            for i in range (len(user)):
                temp[i] = user[i]
            temp[len(user)] = baru
            user = temp
            #sukses didaftarkan
            print("\nUsername ",username,' telah berhasil register ke dalam "Binomo"')

#data = load('eksternal')
#register(data)
