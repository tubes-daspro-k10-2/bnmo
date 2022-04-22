#from utils import *
from utils.main import getLength

arrayGame = [['GAME123','A','Horror','2015','15000','4'],
             ['GAME179','B','RPG','2018','25000','5'],
             ['GAME259','C','Adventure','2020','35000','2'],
             ['GAME297','D','Cooking','2019','45000','3'],
             ['GAME355','E','Cooking','2010','5000','9']]

def search_game_at_store(arrayGame):
    id = input('Masukkan Game ID: ')
    game = input('Masukkan Nama Game: ')
    harga = input('Masukkan Harga Game: ')
    kategori = input('Masukkan Kategori Game: ')
    tahunrilis = input('Masukkan Tahun rilis Game: ')
    
    x = 0
    for i in range (getLength(arrayGame)):
        if ((id == "") or (id == arrayGame[i][0])) and ((game == "") or (game == arrayGame[i][1])) and ((harga == "") or (harga == arrayGame[i][4])) and ((kategori == "") or (kategori == arrayGame[i][2])) and ((tahunrilis == "") or (tahunrilis == arrayGame[i][3])) :
            x = x + 1
            print(f"{x}. {arrayGame[i][0]} | {arrayGame[i][1]} | {arrayGame[i][4]} | {arrayGame[i][2]} | {arrayGame[i][3]} | {arrayGame[i][5]}")
                   
    if x == 0 :
        print('Masukan tidak ditemukan sesuai.')

search_game_at_store(arrayGame)