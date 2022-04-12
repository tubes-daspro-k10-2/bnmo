import os

import time

from utils import *
from utils_ui import *
from utils_file import *

import constants

from f02 import register
from f14 import help
from f15 import Load
from f16 import Save
from f17 import exit

################## VARIABLESSS ####################
width = constants.defaultScreenWidth # constant
userArray = gameArray = riwayatArray = kepemilikanArray = []
# print(userArray, gameArray, kepemilikanArray, riwayatArray)
####################################################


######## PARSER ##########
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('folderName', nargs='?')
args = parser.parse_args()
#print(args.echo)

if args.folderName != None :
    truePath = './'+str(args.folderName)+'/'
    printCenter('Loading ...', width)

    time.sleep(2)

    if(not folderExist(truePath)):
        printWarning(f'folder "{args.folderName}" tidak ditemukan', width)
        time.sleep(1)
    else:
        userArray, gameArray, riwayatArray, kepemilikanArray = Load(truePath)
        print('load result :', userArray, gameArray, riwayatArray, kepemilikanArray)
        time.sleep(1)
    #read_csv(args.folderName)
    #py main.py -folderName ./eksperimen/user.csv
else:
    printWarning('Folder tidak diberikan', width)
    #quit()
##############################


isFinished = False
while not isFinished:
    #header
    header(width)
    print()
    ###################################################
    #print(register(truePath))
    name, username, password = RegisterPage()
    make_csv(truePath, 'user', 0, name, username, password, 4000)

    ########################################
    printCenter('Main Menu', width)

    # account info
    printRight('Account', width)
    print()

    mainChoices()
    print()
    dummiinput = input('Masukkan perintah : ')
    if dummiinput == 'save':
        Save(input())
        print('saving ...')
    elif dummiinput == 'help':
        help()
    elif dummiinput == 'put' :
        (u, n, p) = (input('u '), input('n '), input('p '))
        make_csv(truePath, 'user', 1, u, n, p, 2000)
    elif dummiinput == 'exit':
        exit()
        isFinished = True
    # list of menus to choose
    #1
    #2

    # choice prompt
    printCenter()