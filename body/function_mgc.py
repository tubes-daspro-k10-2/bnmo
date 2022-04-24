import time

# pool response
response = ['ya.', 'tidak.', 'maybe', 'mungkin aja si.', 'menurut kamu?', 'yaaa!', '100!', 'ga dulu deh.', 'bukan keanya :(', 'maap tpi keanya ga :o', 'ya downgs :3', 'keanya belom dulu, semangat! ♥']

# mirip dengan randint, both end included
def lcgInt(minInt : int = 0, maxInt : int = 1) -> int:
    seedInt = 109*(time.time()) # might as well times this by 3
    x = seedInt
    a = 991
    c = 213
    m = 1024 # changeable, found that the optimal value is 7
   
    lcgResult = int(((a*x)+c) % m ) + 1
    #print(seedInt)
    return int(lerp(minInt, maxInt+1, lcgResult/m))

# fungsi yang digunakan untuk melakukan interpolasi dari nilai a ke b dalam nilai t
def lerp(a, b, t):
    return (b-a)*t+a

# prosedur utama
def kerangajaib():
    input('Punya pertanyaan apa nih? ')
    print()
    print(response[lcgInt(0, len(response)-1)])

if __name__ == '__init__' :
    kerangajaib()