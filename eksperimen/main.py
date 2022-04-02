from user import register
from utility_file import *

currentLoginInfo = {}

csv = parse('lmao.csv')

#print(csv[2][2])

if (not register('elmo', 'ferro', 'ferromyass')):
    print('regist failed')
else : 
    print('regis succeed')
    