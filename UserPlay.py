from Clubs import *


def TakeControl(club):
    club.user = True
    

def overwrite():
    return True

def SaveGame_Standard(slot, glob, EURO):
    savepath = f'SAVE_{slot}.dill'
    if os.path.exists(savepath):
        if overwrite():
            os.remove(savepath)
    with open(f'SAVE_{slot}.dill', 'wb') as f:
        dill.dump((ENGLAND, SPAIN, GERMANY, ITALY, \
            FRANCE, PORTUGAL, NETHERLANDS, SCOTLAND, \
            GREECE, TURKIYE, BELGIUM, DENMARK, \
            SWITZERLAND, AUSTRIA, CROATIA, CZECHIA, \
            EURO, glob, RESULTS, DIRECTORY, WINNERS), f)

