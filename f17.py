def exit():
    
    inputDone = False
    while not inputDone:
        try:
            ans = input('Mau save? (y/n) ')
        except:
            pass
        else:
            if isYes(ans) or isNo(ans):
                inputDone = True
    
    if isYes(ans):
        pass
    else : #isNo
        pass

# local function
def isYes(answer : str) :
    if answer == 'y' or answer == 'Y':
        return True
    return False

def isNo(answer : str) :
    if answer == 'n' or answer == 'N':
        return True
    return False
    

    