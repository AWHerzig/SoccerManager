from Competitions import *
# ENGLAND
ENG1 = [  # http://elofootball.com/country.php?countryiso=ENG&season=2023-2024
    CLUB('Manchester City', 'MNC', 95),  # 2397
    CLUB('Liverpool', 'LIV', 92),
    CLUB('Arsenal', 'ARS', 91),
    CLUB('Aston Villa', 'AST', 87),
    CLUB('Tottenham Hotspur', 'TOT', 87),
    CLUB('Manchester United', 'MNU', 84),
    CLUB('Newcastle United', 'NEW', 82),
    CLUB('West Ham United', 'WHU', 80),
    CLUB('Chelsea', 'CHE', 80),
    CLUB('Brighton HA', 'BHA', 79),
    CLUB('Brentford', 'BRE', 76),
    CLUB('Fulham', 'FUL', 76),
    CLUB('Wolverhampton', 'WOL', 75),
    CLUB('Crystal Palace', 'PAL', 72),
    CLUB('Everton', 'EVE', 70),
    CLUB('Bournemouth', 'BOU', 70),
    CLUB('Nottingham Forest', 'FOR', 66),
    CLUB('Burnley', 'BUR', 65),
    CLUB('Luton Town', 'LUT', 63),
    CLUB('Sheffield United', 'SHE', 59),  # 1781
]
ENG2 = [
    CLUB('Leicester City', 'LEI', 69), # 1927
    CLUB('Leeds United', 'LEE', 69),
    CLUB('Ipswich Town', 'IPS', 64),
    CLUB('Southampton', 'SOU', 64),
    CLUB('West Brom', 'BRO', 59),
    CLUB('Norwich City', 'NOR', 60),
    CLUB('Hull City', 'HUL', 56),
    CLUB('Coventry', 'COV', 60),
    CLUB('Middlesbrough', 'MID', 58),
    CLUB('Preston North End', 'PRE', 55), # 1696
    CLUB('Cardiff City', 'CAR', 51),
    CLUB('Bristol City', 'BRI', 56),
    CLUB('Sunderland', 'SUN', 54),
    CLUB('Swansea City', 'SWA', 56),
    CLUB('Watford', 'WAT', 54),
    CLUB('Millwall', 'MIL', 52),
    CLUB('Stoke City', 'STO', 52),
    CLUB('Queens Park Rangers', 'QPR', 49),
    CLUB('Blackburn Rovers', 'BLA', 53),
    CLUB('Plymouth Argyle', 'PLY', 51),
    CLUB('Sheffield Wednesday', 'WED', 54),
    CLUB('Birmingham City', 'BIR', 48), 
    CLUB('Huddersfield Town', 'HUD', 48),  # 1614
    CLUB('Rotherham', 'ROT', 40)  # 1506
]
ENG3 = [
    CLUB('Portsmouth', 'POR', 53), #1673
    CLUB('Derby County', 'DER', 53),
    CLUB('Bolton Wanderers', 'BOL', 51),
    CLUB('Peterborough', 'PET', 47),
    CLUB('Barnsley', 'BAR', 46),  # 1587
    CLUB('Oxford United', 'OXF', 44),
    CLUB('Lincoln City', 'LIN', 48),
    CLUB('Blackpool', 'BLA', 47),
    CLUB('Stevenage', 'STE', 40),
    CLUB('Wycombe', 'WYC', 43),
    CLUB('Leyton Orient', 'LEY', 39),
    CLUB('Wigan Athletic', 'WIG', 44),
    CLUB('Exeter City', 'EXE', 41), # 1521
    CLUB('Northampton', 'NOR', 37),
    CLUB('Bristol Rovers', 'BRR', 35), # 1439
    CLUB('Charlton', 'CHA', 40),
    CLUB('Reading', 'REA', 41),
    CLUB('Cambridge United', 'CAM', 34),
    CLUB('Shrewsbury', 'SHR', 33),
    CLUB('Burton', 'BTN', 32),
    CLUB('Cheltenham', 'CNM', 33),
    CLUB('Fleetwood', 'FLE', 34),
    CLUB('Port Vale', 'POV', 30), # 1372
    CLUB('Carlisle', 'CAR', 26)  # 1329
]
ENG4 = [
    CLUB('Stockport', 'STO', 42),  # 1547
    CLUB('Mansfield Town', 'MAN', 39),
    CLUB('Wrexham', 'WRE', 40), # 1517
    CLUB('Milton Keynes', 'MK', 36),
    CLUB('Doncaster', 'DON', 34),
    CLUB('Crewe Alexandra', 'CRE', 28),
    CLUB('Barrow', 'BRW', 26),
    CLUB('Crawley Town', 'CRA', 31),
    CLUB('Bradford City', 'BRD', 31), # 1391
    CLUB('Walsall', 'WAL', 28),
    CLUB('Gillingham', 'GIL', 27),
    CLUB('AFC Wimbledon', 'WIM', 27),
    CLUB('Harrogate Town', 'HAR', 24),
    CLUB('Notts County', 'NOT', 26),
    CLUB('Tranmere', 'TRA', 25),  # 1346
    CLUB('Morecambe', 'MOR', 24),
    CLUB('Newport County', 'NPT', 22),
    CLUB('Accrington Stanley', 'ACC', 21),
    CLUB('Swindon Town', 'SWI', 20),  # 1302
    CLUB('Salford City', 'SAL', 25),
    CLUB('Grimsby Town', 'GRI', 22),
    CLUB('Colchester', 'COL', 18),
    CLUB('Sutton United', 'SUT', 20),
    CLUB('Forest Green', 'FOR', 16)  # 1252
]
ENGLAND = ASSOCIATION('England', 'ENG', leagues=[ENG1, ENG2, ENG3, ENG4], relSpots=[3, 3, 4], lastSpot=1, euroSpots=[4, 2, 1])
# SPAIN
