from utils.file import getIndexByName
from utils.main import getLength
from constants import emptySessionAccount


def isAdmin(sessionAccount : list) -> bool:
    if sessionAccount[3] == 'admin':
        return True
    return False

def isUsernameValid(s):
    if s == '':
        return False

    for i in s:
        if (i=='-' or i=='_' or 'a'<=i<='z' or 'A'<=i<='Z' or '0'<=i<='9'):
            continue
        else:
            return False
    return True

# def isInputValid(s):
#     if s == '':
#         return False

#     for i in s:
#         if (i == ' ' or i == ';'):
#             return False

#     return True


def getSessionAccount(userArray, username):
    ada = False
    i=0
    while ((not ada) and i < getLength(userArray)):
        if (userArray[i][getIndexByName('username', 'user')] == username):
            ada = True
            
            # tangkep nilainya di main
            return userArray[i][getIndexByName('username', 'user')], userArray[i][getIndexByName('name', 'user')], userArray[i][getIndexByName('saldo', 'user')], userArray[i][getIndexByName('role', 'user')], userArray[i][getIndexByName('id', 'user')] #username, name, saldo, role       
        i += 1
    return emptySessionAccount