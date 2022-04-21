#Load File
import os
from parse import *

#Load 1 folder berisi file-file eksternal
def load(folder):
  n = os.getcwd()
  if folder != '.':
    os.chdir(folder)
  user = openCSV("user.csv", "r")
  game = openCSV("game.csv", "r")
  os.chdir(n)
  return (user,game)


#data :
#     data[0] : user.csv
#     data[1] : game.csv
#data= load('eksternal')
#print(data[1])