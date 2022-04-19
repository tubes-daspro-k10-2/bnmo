import time

response = ['ya', 'tidak', 'maybe', 'magic', 'conch', 'shell']

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

def lerp(a, b, t):
    return (b-a)*t+a

# for i in range(10):
#     print(response[lcgInt(0, len(response))])
#     time.sleep(0.1)

input('Punya pertanyaan apa nih? ')
print(response[lcgInt(0, len(response)-1)])