# load
# needs user.csv, game.csv, riwayat.csv, kepemilikan.csv

import os
from utils_file import *

def Load(folderArg : str) -> tuple[list]:
    userArr = read_csv(folderArg, 'user')
    gameArr = read_csv(folderArg, 'game')
    riwayatArr = read_csv(folderArg, 'riwayat')
    kepemilikanArr = read_csv(folderArg, 'kepemilikan')
    
    print('success')

    return (userArr, gameArr, riwayatArr, kepemilikanArr)

def folderExist(folderArg : str) -> bool :
    for (root, dirs, files) in os.walk(folderArg, topdown=True):
        if root == folderArg:
            return True
        
    return False


#folderExist('.')