import os

from utils import *
from utils_ui import *
from utils_user import *

import f15

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
    if(not f15.folderExist(truePath)):
        print(f'folder "{args.folderName}" tidak ditemukan')
    else:
        f15.Load(truePath)
    #read_csv(args.folderName)
    #py main.py -folderName ./eksperimen/user.csv
else:
    printCenter('Folder tidak diberikan', width)
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
input('Masukkan perintah : ')

# list of menus to choose
#1
#2

# choice prompt
printCenter()