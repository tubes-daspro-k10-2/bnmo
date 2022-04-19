import os
import time

#from utils import 
from utils.ui import printWarning, printRight, printCenter, clearScreen
from utils.file import append_array, folderExist # move it to save

from front.ui import LoginPage, header, RegisterPage, LandingPage, MainMenu

import constants

from body.function_main import help ,Load, Save, exit

from f02 import register
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
    sessionAccount = ['','',] #username, name, saldo
    folderPath = ''

    print(args)
    if args.folderName != None :
        folderPath = './'+str(args.folderName)+'/'
        printCenter('Loading ...')

        time.sleep(2)

        if(not folderExist(folderPath)):
            printWarning(f'folder "{args.folderName}" tidak ditemukan')
            time.sleep(1)
        else:
            userArray, gameArray, riwayatArray, kepemilikanArray = Load(folderPath)
            print('load result :', userArray, gameArray, riwayatArray, kepemilikanArray) # hapus ini
            time.sleep(1)
        #read_csv(args.folderName)
        #py main.py -folderName ./eksperimen/user.csv
    else:
        printWarning('Folder tidak diberikan')
        #quit()
    ##############################


    finished = False
    while not finished:
        clearScreen()
        currentAnswer : str = ''
        #header
        header()
        print()
        ###################################################
        
        if sessionAccount[0] == '':
            name = username = password = ''
            currentAnswer = LandingPage() # login, register, exit
            if currentAnswer == 1:
                LoginPage()
            elif currentAnswer == 2:
                name, username, password = RegisterPage()
            else:
                exit(folderPath, userArray)
                finished = True
            sessionAccount = username, name, 0      
            userArray = append_array(userArray, 0, name, username, password, 4000)
        else :
            dummiinput = MainMenu(sessionAccount)
            if dummiinput == 'help':
                help()
            elif dummiinput == 'put' :
                (u, n, p) = (input('u '), input('n '), input('p '))
                userArray = append_array(folderPath, 'user', 1, u, n, p, 2000)
            elif dummiinput == 'exit':
                exit(folderPath, userArray)
                clearScreen()
                finished = True

        ########################################
        
        # list of menus to choose
        #1
        #2

        # choice prompt
        printCenter()


if __name__ == '__main__':
    main()