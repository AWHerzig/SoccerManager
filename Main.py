from Clubs import *

Associations = [ENGLAND]
DIRECTORY.to_csv('Output/Directory.csv', index=False)
WINNERS.to_csv('Output/Winners.csv', index=False)

def yearReset():
    for assoc in Associations:
        assoc.endOfYear()
    DIRECTORY.to_csv('Output/Directory.csv', index=False)
    WINNERS.to_csv('Output/Winners.csv', index=False)



