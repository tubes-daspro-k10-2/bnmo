def isAdmin(sessionAccount : list) -> bool:
    if sessionAccount[3] == 'admin':
        return True
    return False

def isUsernameValid(s):
    for i in s:
        if (i=='-' or i=='_' or 'a'<=i<='z' or 'A'<=i<='Z' or '0'<=i<='9'):
            continue
        else:
            return False
    return True