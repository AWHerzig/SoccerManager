from Clubs import *

TIERA = [ENGLAND, SPAIN, GERMANY, ITALY]
TIERB = [FRANCE, PORTUGAL]
TIERC = [NETHERLANDS, SCOTLAND, GREECE, TURKIYE, BELGIUM, 
    DENMARK, SWITZERLAND, AUSTRIA, CROATIA, CZECHIA]
ALL = TIERA + TIERB + TIERC
DIRECTORY.to_csv('Output/Directory.csv', index=False)
WINNERS.to_csv('Output/Winners.csv', index=False)

def yearReset():
    for assoc in ALL:
        assoc.endOfYear()
    DIRECTORY.to_csv('Output/Directory.csv', index=False)
    WINNERS.to_csv('Output/Winners.csv', index=False)



