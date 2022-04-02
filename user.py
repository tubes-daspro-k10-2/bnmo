from utility_file import *
from utility_user import *

# id, username, nama, password, saldo

def register(username : str, nama : str, password : str) -> bool:
    userDatabase = parse('user.csv')
    
    if validate_username(username):
        for i in range(len(userDatabase)):
            if username == userDatabase[i][1]:
                return False # failed

        # input to csv
        write_csv('user.csv', 1, username, nama, password, 1000)
        return True
            
        
        
