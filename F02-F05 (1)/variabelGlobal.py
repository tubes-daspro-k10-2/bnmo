login = False

id = ''
nama = ''
username = ''
password = ''
role = ''
saldo = 0

def init():
    global login

    global id
    global username
    global nama
    global password
    global role
    global saldo

def len(a):
  n=0
  for i in a:
    if i!="NaN":
      n+=1
  return n
