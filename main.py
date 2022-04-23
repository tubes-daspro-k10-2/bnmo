import os
import time

#from utils import 
from utils.ui import printWarning, printRight, printCenter, clearScreen
from utils.file import append_array, folderExist, getIndexByName # move it to save
from utils.user import getSessionAccount, isAdmin

from front.ui import ExitPage, LoginPage, RegisterPage, header, RegisterPage, LandingPage, MainMenu

from constants import emptySessionAccount

from body.function_main import register, login, riwayat, search_game_at_store, search_my_game, tambah_game, topup, ubah_game, ubah_stok, list_game_toko, buy_game, list_game, help , Load, Save, exit

#from f02 import register
#from f14 import help
#from f15 import Load
#from f16 import Save
#from f17 import exit

######## PARSER ##########
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('folderName', nargs='?')
args = parser.parse_args()
#print(args.echo)

def main():
    sessionAccount = emptySessionAccount #username, name, saldo, role, id
    folderPath = ''

    if args.folderName != None :
        folderPath = './'+str(args.folderName)+'/'
        printCenter('Loading ...')

        time.sleep(2)

        if(not folderExist(folderPath)):
            printWarning(f'folder "{args.folderName}" tidak ditemukan')
            time.sleep(1)
            quit()
        else:
            userArray, gameArray, riwayatArray, kepemilikanArray = Load(folderPath)
            # print('load result :', userArray, gameArray, riwayatArray, kepemilikanArray) # hapus ini
            time.sleep(1)
        #read_csv(args.folderName)
        #py main.py -folderName ./eksperimen/user.csv
    else:
        printWarning('Folder tidak diberikan')
        quit()
    ##############################


    finished = False
    while not finished:
        
        #clearScreen()
        choiceAnswer : str = ''
        #header
        header()
        print()
        ###################################################
        name = username = password = ''
        # Belum memiliki sesi login akun
        if sessionAccount[0] == '':
            choiceAnswer = LandingPage() # login, register, exit
            if choiceAnswer == 1:
                username, password = LoginPage()
                sessionAccount = login(userArray, username, password)
            # elif currentAnswer == 2:
            #     name, username, password = RegisterPage()
            else: # 2
                exit(folderPath, userArray, gameArray, riwayatArray, kepemilikanArray)
                finished = True
            #sessionAccount = username, name, 0      
            #userArray = append_array(userArray, 0, name, username, password, 4000)

            # print(sessionAccount)
            #exit(folderPath, userArray)
        else :
            choiceAnswer = MainMenu(sessionAccount)
            

            if isAdmin(sessionAccount):
                if choiceAnswer == 1 :
                    name, username, password = RegisterPage()
                    userArray = register(userArray, name, username, password)
                elif choiceAnswer == 2:
                    gameArray = tambah_game(gameArray)
                elif choiceAnswer == 3:
                    gameArray = ubah_game(gameArray)
                elif choiceAnswer == 4:
                    gameArray = ubah_stok(gameArray)
                elif choiceAnswer == 5:
                    list_game_toko(gameArray)
                elif choiceAnswer == 6:
                    search_game_at_store(gameArray)
                elif choiceAnswer == 7:
                    userArray = topup(userArray)
                    print(userArray)
                elif choiceAnswer == 8:
                    help()
                elif choiceAnswer == 9:
                    Save(folderPath, userArray, gameArray, riwayatArray, kepemilikanArray)
                elif choiceAnswer == 10:
                    exit(folderPath, userArray, gameArray, riwayatArray, kepemilikanArray)
                    clearScreen()
                    finished = True
            else:
                if choiceAnswer == 1:
                    list_game_toko(gameArray)
                elif choiceAnswer == 2:
                    gameArray, kepemilikanArray, userArray = buy_game(gameArray, kepemilikanArray, userArray, sessionAccount[4]) 
                elif choiceAnswer == 3:
                    list_game(gameArray, kepemilikanArray, sessionAccount[4])
                elif choiceAnswer == 4:
                    search_my_game(gameArray, kepemilikanArray, sessionAccount[4])
                elif choiceAnswer == 5:
                    search_game_at_store(gameArray)
                elif choiceAnswer == 6:
                    riwayat(riwayatArray, sessionAccount[4])
                elif choiceAnswer == 8:
                    help()
                elif choiceAnswer == 9:
                    Save(folderPath, userArray, gameArray, riwayatArray, kepemilikanArray)
                elif choiceAnswer == 10:
                    exit(folderPath, userArray, gameArray, riwayatArray, kepemilikanArray)
                    #clearScreen()
                    finished = True
            
            if finished : ExitPage()

            input()
            clearScreen()
            sessionAccount = getSessionAccount(userArray, sessionAccount[0])
        ########################################
        
        # list of menus to choose
        #1
        #2

        # choice prompt
        # printCenter()


if __name__ == '__main__':
    main()