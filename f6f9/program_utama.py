from main_function import *
from side_function import *

def check_access(id) :
    k = 0
    found = False
    global user_data
    while (k < length(user_data)) and found == False :
        if user_data[k][0] == id :
            found = True
            access = user_data[k][4]
        k += 1
    return access
    
# Mengidentifikasi command yang dimasukkan
def identify(command, matrix1, matrix2, matrix3): # matriks 1 - data untuk game; matriks 2 - data untuk kepemilikan
    global user_id
    if command == "ubah_stok" :
        if check_access(user_id) == "admin" :
            ubah_stok(matrix1) # game_data
        else :
            print("Maaf, kamu tidak memiliki akses.")
    elif command == "list_game_toko" :
        list_game_toko(matrix1) # game_data
    elif command == "buy_game" :
        if check_access(user_id) == "user" :
            global kepemilikan_data # untuk merubah kepemilikan_data didalam fungsi
            kepemilikan_data = buy_game(matrix1, matrix2, matrix3, user_id) # game_data, kepemilikan_data, user_id
        else :
            print("Maaf, perintah ini hanya bisa digunakan oleh user.")
    elif command == "list_game" :
        if check_access(user_id) == "user" :
            list_game(matrix1, matrix2, user_id)
        else :
            print("Maaf, perintah ini hanya bisa digunakan oleh user.")

# Merubah data pada CSV menjadi bentuk matriks
game_data = convert_csv("game.csv")
kepemilikan_data = convert_csv("kepemilikan.csv")
user_data = convert_csv("user.csv")

# Loop input command
user_id = 16521888 # id yang didapatkan saat perintah login
loop = True

while loop == True :
    # print(game_data,kepemilikan_data, user_data)
    N = input(">>> ") # menginput command
    if N == "exit":
        loop = False
    else :
        identify(N, game_data, kepemilikan_data, user_data) # mengidentifikasi command
