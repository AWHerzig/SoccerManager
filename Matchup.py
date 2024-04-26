from DirWide import *



TacticMatchup = {
    'HomeTactic':     ['Park The Bus', 'Counter Attack', 'Width', 'Strangle', 'No Tactic'],
    'Park The Bus':   [(0, 'quality'), (0, 'quality'), (25, 'draw'), (50, 'draw'), (-100, 'draw')],
    'Counter Attack': [(0, 'quality'), (0, 'quality'), (-25, 'sharp'), (0, 'sharp'), (-100, 'sharp')],
    'Width':          [(-25, 'draw'), (25, 'sharp'), (0, 'quality'), (0, 'quality'), (-100, 'quality')],
    'Strangle':       [(-50, 'draw'), (0, 'sharp'), (0, 'quality'), (0, 'quality'), (-100, 'quality')],
    'No Tactic':      [(100, 'draw'), (100, 'sharp'), (100, 'quality'), (100, 'quality'), (0, 'quality')]
}
TMdf = pandas.DataFrame(TacticMatchup).set_index('HomeTactic')