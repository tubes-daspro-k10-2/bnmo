# #lcg
import time
def lcgInt(minInt, maxInt):
    seedInt = (time.monotonic())
    x = seedInt
    a = 3
    c = 1
    m = 7 # found optimal to be 7
    # arr = [0 for i in range(1,25)]
    # for i in range(1,39):
    #     #arr[LCG] +=1
    #     #print (x)
    #     x = x +1

    LCG = int(((a*x)+c) % m ) + 1

    return int(lerp(minInt, maxInt, LCG/m))
    # print(LCG)
    # print(time.monotonic())

def lerp(a, b, t)   :
    return (t*(b-a)+a)

print(lcgInt(1,4))
# #print(arr)

# def asd(s1,s2):
#     seedInt = 2
#     x = seedInt
#     a = 3
#     c = 1
#     m = abs(s2-s1)+1
#     for i in range(1,22):
#         LCG = int( ((a*x)+c) % m )
#         print(LCG + s1)
#         #print (x)
#         x = x +1
        
# asd(0,19)