from utils.file import read_csv, folderExist, createFolder, save_csv
from utils.ui import printWarning

#f14
def help():
    printWarning('HELP MESSAGE', 100)

#f15
def Load(folderArg : str) -> tuple[list, list, list, list]:
    userArr = read_csv(folderArg, 'user')
    gameArr = read_csv(folderArg, 'game')
    riwayatArr = read_csv(folderArg, 'riwayat')
    kepemilikanArr = read_csv(folderArg, 'kepemilikan')
    
    printWarning('Data from ' + folderArg + ' loaded successfully.')

    return (userArr, gameArr, riwayatArr, kepemilikanArr) # tuple, be careful

#f16
def Save(folderArg : str, userArray : list):
    #folderArg = './'+ folderArg +'/' # is alr made ./{}/
    
    if folderExist(folderArg):
        save_csv(folderArg, 'user', userArray)
    else: #folder doesnt exist
        createFolder(folderArg)

#f17
def exit(folderPath : str, userArray : list):
    # local function
    def isYes(answer : str) :
        if answer == 'y' or answer == 'Y':
            return True
        return False

    def isNo(answer : str) :
        if answer == 'n' or answer == 'N':
            return True
        return False
    
    inputDone = False
    while not inputDone:
        try:
            ans = input('Mau save? (y/n) ')
        except:
            pass
        else:
            if isYes(ans) or isNo(ans):
                inputDone = True

    if isYes(ans):
        Save(folderPath, userArray)

    