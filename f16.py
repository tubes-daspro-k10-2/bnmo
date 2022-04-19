# save
from utility.utils_file import folderExist, createFolder
# def folderExist(folderArg : str) -> bool :
#     for (root, dirs, files) in os.walk(folderArg, topdown=True):
#         if root == folderArg:
#             return True
        
#     return False
# folderArg = './'
# for (root, dirs, files) in os.walk(folderArg, topdown=True):
#     print(root, dirs, files)

def Save(folderArg : str):
    folderArg = './'+ folderArg +'/'
    
    if folderExist(folderArg):
        pass
    else: #folder doesnt exist
        createFolder(folderArg)