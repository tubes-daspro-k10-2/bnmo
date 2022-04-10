# F2 - Register
alphabet = "abcdefghijklmnopqrstuvwxyz"
numbersymbol = "0123456789-_"

def getlength(list1):
    length = 0
    for i in list1:
        length +=1
    return length

def mergelist(list1,list2):
    listinlist = [list2]
    mergedlist = list1 + listinlist
    return mergedlist

def register(dfuser):
    nama = input("Masukan nama: ")
    username = input("Masukan username: ")
    password = input("Masukan password: ")

    # Menghitung panjang dfuser
    length = getlength(dfuser)

    # Melakukan cek apakah terdapat username yang sama
    sameuser = False
    for i in range(length):
        if (dfuser[i][1] == username):
            sameuser = True
    while (sameuser == True):
        sameuser = False
        print("Username", username," sudah terpakai, silakan menggunakan username lain.")
        username = input("Masukan username: ")
        for i in dfuser["username"]:
            if (i == username):
                sameuser = True
            
    
    uservalid = True
    # Melakukan cek validitas username
    for i in username:
        if (i not in (alphabet) and i not in (alphabet.upper()) and i not in (numbersymbol)):
            uservalid = False
    while (uservalid == False):
        print("Username", username, "tidak valid. Username hanya diperkenankan mengandung alphabet, angka, underscore, dan strip")
        username = input("Masukan username: ")
        uservalid = True
        for i in username:
            if (i not in (alphabet) and i not in (alphabet.upper()) and i not in (numbersymbol)):
                uservalid = False


    # Melakukan penggabungan 2 list
    newid = length
    newuserlist = [str(newid), username, nama, password, "user", "0"]
    mergedlist = mergelist(dfuser, newuserlist)
    print("Username", username,' telah berhasil register ke dalam "Binomo".')
    return mergedlist
