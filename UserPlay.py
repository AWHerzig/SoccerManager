from Clubs import *


def TakeControl(club):
    club.user = True
    base = club.baserating / 11
    club.squadGK  = [GK(base), GK(base-10), GK(base - 20)]
    club.squadDEF = [DEF(base) for i in range(4)] + [DEF(base - 10) for i in range(4)]
    club.squadMID = [MID(base) for i in range(4)] + [MID(base - 10) for i in range(4)]
    club.squadATT = [ATT(base) for i in range(4)] + [ATT(base - 10) for i in range(4)]

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

