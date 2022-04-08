import os

import time

from utils import *
from utils_ui import *
from utils_file import *

from f15 import Load
from f16 import Save

width = 100 # constant

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
        print(Load(truePath))
        time.sleep(1)
    #read_csv(args.folderName)
    #py main.py -folderName ./eksperimen/user.csv
else:
    printWarning('Folder tidak diberikan', width)
    #quit()
##############################




#header
header(width)
print()

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
elif dummiinput == 'put' :
    make_csv(truePath, 'user', 1, 'username', 'nama', 'password', 1000)
# list of menus to choose
#1
#2

# choice prompt
printCenter()