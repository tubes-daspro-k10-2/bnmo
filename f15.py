import os
def Load(folderArg):
    print('success')

def folderExist(folderArg : str) -> bool :
    for (root, dirs, files) in os.walk(folderArg, topdown=True):
        if root == folderArg:
            return True
        
    return False

#folderExist('.')