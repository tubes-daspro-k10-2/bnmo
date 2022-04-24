from utils.file import getIndexByName
from utils.main import getLength
from constants import emptySessionAccount


def isAdmin(sessionAccount : list) -> bool:
    # fungsi yang berguna untuk menentukan apakah sesi akun sekarang memiliki role admin

    if sessionAccount[3] == 'admin':
        return True

    return False

def isUsernameValid(s):
    # fungsi yang menentukan paakah username yang dimasukan valid
    if s == '':
        return False

    for i in s:
        if (i=='-' or i=='_' or 'a'<=i<='z' or 'A'<=i<='Z' or '0'<=i<='9'):
            continue
        else:
            return False
    return True

def getSessionAccount(userArray, username):
    # fungsi yange menentukan apakah sesi akun valid
    ada = False
    i=0

    # cari value pengguna yang diinginkan
    while ((not ada) and i < getLength(userArray)):
        if (userArray[i][getIndexByName('username', 'user')] == username):
            ada = True
            
            # return nilai sesi akun yang bersesuaian
            return userArray[i][getIndexByName('username', 'user')], userArray[i][getIndexByName('name', 'user')], userArray[i][getIndexByName('saldo', 'user')], userArray[i][getIndexByName('role', 'user')], userArray[i][getIndexByName('id', 'user')] #username, name, saldo, role       
        i += 1

    # pengguna yang dimaksud tidak ditemukan
    return emptySessionAccount