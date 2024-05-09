from Competitions import *
## TIER A ----
# ENGLAND
ENG1 = [  # http://elofootball.com/country.php?countryiso=ENG&season=2023-2024
    CLUB('Manchester City', 'MNC', 99),  # 2397
    CLUB('Liverpool', 'LIV', 94),  # 2252
    CLUB('Arsenal', 'ARS', 93),
    CLUB('Aston Villa', 'AST', 87),  # 2111
    CLUB('Tottenham Hotspur', 'TOT', 87),
    CLUB('Manchester United', 'MNU', 84),
    CLUB('Newcastle United', 'NEW', 82),
    CLUB('West Ham United', 'WHU', 80),
    CLUB('Chelsea', 'CHE', 80),
    CLUB('Brighton HA', 'BHA', 79),
    CLUB('Brentford', 'BRE', 76), # 1985
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
ENGLAND = ASSOCIATION('England', 'ENG', leagues=[ENG1, ENG2, ENG3, ENG4], relSpots=[3, 3, 4], lastSpot='ENG')
# SPAIN
ESP1 = [
    CLUB('Real Madrid', 'RMA', 97),  # 2348
    CLUB('FC Barcelona', 'FCB', 90),  # 2182
    CLUB('Girona', 'GIR', 85),
    CLUB('Atletico Madrid', 'ATL', 88),
    CLUB('AC Bilbao', 'BIL', 87), 
    CLUB('Real Sociedad', 'SOC', 83),
    CLUB('Real Betis', 'BET', 78),
    CLUB('Valencia', 'VAL', 76),
    CLUB('Villarreal', 'VIL', 80), # 2038
    CLUB('Getafe', 'GET', 70), # 1934
    CLUB('Osasuna', 'OSA', 69),
    CLUB('Alaves', 'ALA', 67),
    CLUB('Sevilla', 'SEV', 78),
    CLUB('Las Palmas', 'PAL', 65),
    CLUB('Rayo Vallecano', 'RAY', 65),
    CLUB('Mallorca', 'MAL', 72),
    CLUB('Celta Vigo', 'CEL', 71),
    CLUB('Cadiz', 'CAD', 65),
    CLUB('Granada', 'GRA', 61), # 1802
    CLUB('Almeria', 'ALM', 60),
]
ESP2 = [
    CLUB('Leganes', 'LEG', 61),
    CLUB('Valladolid', 'VDD', 64),
    CLUB('Eibar', 'EIB', 63),
    CLUB('Espanyol', 'ESP', 64),
    CLUB('Elche', 'ELC', 61),
    CLUB('Racing Santander', 'RCS', 56), # 1745
    CLUB('Sporting Gijon', 'GIJ', 56),
    CLUB('Real Oviedo', 'OVI', 60),
    CLUB('Burgos', 'BUR', 55),
    CLUB('Racing Ferrol', 'RCF', 53), # 1708
    CLUB('Levante', 'LEV', 61),
    CLUB('Tenerife', 'TEN', 55),
    CLUB('Real Zaragoza', 'ZAR', 54),
    CLUB('Eldense', 'ELD', 49),
    CLUB('FC Cartagena', 'CAR', 52),
    CLUB('Huesca', 'HUE', 55),
    CLUB('Mirandes', 'MIR', 50),
    CLUB('Alcorcon', 'ALC', 49),
    CLUB('Albacete', 'ALB', 51),
    CLUB('Villarreal B', 'VIL-B', 48),
    CLUB('Amorebieta', 'AMO', 50),
    CLUB('Andorra', 'AND', 50)
]
SPAIN = ASSOCIATION('Spain', 'ESP', leagues = [ESP1, ESP2], relSpots = [3], lastSpot = 'ESP')
# GERMANY
GER1 = [
    CLUB('Leverkusen', 'LEV', 94), # 2246
    CLUB('Bayern Munich', 'BAY', 93),
    CLUB('VfB Stuttgart', 'STU', 83),
    CLUB('RB Leipzig', 'LEI', 90),
    CLUB('Borrusia Dortmund', 'BVB', 91),
    CLUB('Eintracht Frankfurt', 'EIN', 74),
    CLUB('SC Freiburg', 'FRE', 74),
    CLUB('Augsburg', 'AUG', 67),
    CLUB('Hoffenheim', 'HOF', 69),
    CLUB('Werder Bremen', 'WER', 66),
    CLUB('Heidenheim', 'HEI', 65), # 1876
    CLUB('Wolfsburg', 'WOL', 68),
    CLUB('Monchengladbach', 'MON', 69), # 1912
    CLUB('Union Berlin', 'UNI', 67),
    CLUB('VfL Bochum', 'BOC', 63), # 1837
    CLUB('Mainz', 'MAI', 67),
    CLUB('Koln', 'KOL', 64),
    CLUB('Darmstadt', 'DAR', 56) # 1754
]
GER2 = [
    CLUB('FC St. Pauli', 'StP', 65),
    CLUB('Holstein Kiel', 'KIE', 64),
    CLUB('Dusseldorf', 'DUS', 65),
    CLUB('Hamburger SV', 'HSV', 59),
    CLUB('Karlsruher', 'KAR', 57), # 1767
    CLUB('Hannover 96', 'HAN', 54), # 1729
    CLUB('Paderborn', 'PAD', 56),
    CLUB('Hertha Berlin', 'HER', 58),
    CLUB('Greuther Furth', 'FUR', 49), # 1669
    CLUB('SV Elversberg', 'ELV', 48),
    CLUB('FC Magdeburg', 'MAG', 50),
    CLUB('FC Schalke', 'S04', 54),
    CLUB('Nurnberg', 'FCN', 46),
    CLUB('Eintracht Braunschweig', 'EBW', 47),
    CLUB('Kaiserslautern', 'FCK', 49),
    CLUB('Wehen Wiesbaden', 'WIE', 45),
    CLUB('Hansa', 'HAN', 42), # 1580
    CLUB('Osnabruck', 'OSN', 41)
]
GER3 = [
    CLUB('SSV Ulm', 'ULM'),
    CLUB('Jahn Regensburg', 'REG'),
    CLUB('Preuben Munster', 'MUN'),
    CLUB('Rot-Weiss Essen', 'RWE'),
    CLUB('Dynamo Dresden', 'DYN'),
    CLUB('Saarbrucken', 'SAA'),
    CLUB('Erzgebirge Aue', 'ERZ'),
    CLUB('Unterhaching', 'UNT'),
    CLUB('SV Sandhausen', 'SAN'),
    CLUB('Borussia Dortmund 2', 'BVB2'),
    CLUB('Ingolstadt', 'ING'),
    CLUB('Viktoria Koln', 'VIK'),
    CLUB('Verl', 'VER'),
    CLUB('1860 Munich', '1860'),
    CLUB('Arminia', 'ARM'),
    CLUB('SV Waldhof', 'WAL'),
    CLUB('Hallescher', 'HAL'),
    CLUB('MSV Duisburg', 'DUI'),
    CLUB('Lubeck', 'LUB'),
    CLUB('SC Freiburg 2', 'FRE2')
]
GERMANY = ASSOCIATION('Germany', 'GER', leagues = [GER1, GER2, GER3], relSpots = [3, 3], lastSpot = 'GER')
# ITALY

ITA1 = [
    CLUB('Internazionale', 'INT'),
    CLUB('AC Milan', 'ACM'),
    CLUB('Juventus', 'JUV'),
    CLUB('Bolonga', 'BOL'),
    CLUB('Roma', 'ROM'),
    CLUB('Atalanta', 'ATA'),
    CLUB('Lazio', 'LAZ'),
    CLUB('Fiorentina', 'FIO'),
    CLUB('Napoli', 'NAP'),
    CLUB('Torino', 'TOR'),
    CLUB('Monza', 'MON'),
    CLUB('Genoa', 'GEN'),
    CLUB('Lecce', 'LEC'),
    CLUB('Cagliari', 'CAG'),
    CLUB('Verona', 'VER'),
    CLUB('Frosinone', 'FRO'),
    CLUB('Empoli', 'EMP'),
    CLUB('Udinese', 'UDI'),
    CLUB('Sassuolo', 'SAS'),
    CLUB('Salernitana', 'SAL')
]
ITA2 = [
    CLUB('Parma', 'PAR'),
    CLUB('Como', 'COM'),
    CLUB('Venezia', 'VEN'),
    CLUB('Cremonese', 'CRE'),
    CLUB('Catanzaro', 'CAT'),
    CLUB('Palermo', 'PAL'),
    CLUB('Sampdoria', 'SAM'),
    CLUB('Brescia', 'BRE'),
    CLUB('Sudtirol', 'SUD'),
    CLUB('Reggiana', 'REG'),
    CLUB('Cosenza', 'COS'),
    CLUB('Pisa', 'PIS'),
    CLUB('Cittadella', 'CIT'),
    CLUB('Modena', 'MOD'),
    CLUB('Spezia', 'SPE'),
    CLUB('Ascoli', 'ASC'),
    CLUB('Ternana', 'TER'),
    CLUB('Bari', 'BAR'),
    CLUB('FeralpiSalo', 'FS'), # What kind of a name is this
    CLUB('Lecco', 'LEC')
]
ITALY = ASSOCIATION('Italy', 'ITA', leagues = [ITA1, ITA2], relSpots = [3], lastSpot = 'ESP')
# Okay so italy has their own different promotion playoffs but its suuuuper weird so I'm ignoring the first round and the 14-points clear rule, then its just ESP

## TIER B ----
# FRANCE
FRA1 = [
    CLUB('Paris St-Germain', 'PSG'),
    CLUB('Monaco', 'MON'),
    CLUB('Brest', 'BRE'),
    CLUB('LOSC Lille', 'LIL'),
    CLUB('Nice', 'NIC'),
    CLUB('Lens', 'LEN'),
    CLUB('Olympique Marseille', 'OM'),
    CLUB('Olympique Lyon', 'OL'),
    CLUB('Rennes', 'REN'),
    CLUB('Toulouse', 'TOU'),
    CLUB('Reims', 'REI'),
    CLUB('Montpellier', 'MTP'),
    CLUB('Strasbourg', 'STR'),
    CLUB('Nantes', 'NAN'),
    CLUB('Le Havre', 'HAV'),
    CLUB('Metz', 'MET'),
    CLUB('Lorient', 'LOR'),
    CLUB('Clermont Foot', 'CLE')
]
FRA2 = [
    CLUB('Auxerre', 'AUX'),
    CLUB('St-Etienne', 'StE'),
    CLUB('Angers', 'ANG'),
    CLUB('Rodez', 'ROD'),
    CLUB('Paris FC', 'PAR'),
    CLUB('Stade Laval', 'LAV'),
    CLUB('Pau', 'PAU'),
    CLUB('Caen','CAE'),
    CLUB('Guingamp', 'GUI'),
    CLUB('Amiens SC', 'AMI'),
    CLUB('Ajaccio', 'AJA'),
    CLUB('Bastia', 'BAS'),
    CLUB('Grenoble Foot','GRE'),
    CLUB('Bordeaux', 'BOR'),
    CLUB('Annecy', 'ANN'),
    CLUB('Dunkerque', 'DUN'),
    CLUB('Troyes', 'TRY'),
    CLUB('Quevilly-Rouen', 'QUE'),
    CLUB('Concarneau', 'CON'),
    CLUB('Valenciennes', 'VAFC')
]
FRANCE = ASSOCIATION('France', 'FRA', leagues = [FRA1, FRA2], relSpots = [3], lastSpot = 'GER')
# France also has a weird Playoff system I'm ignoring the first round of, Germany's gets the point of it
# PORTUGAL
POR1 = [
    CLUB('Sporting CP', 'SCP'),
    CLUB('Benfica', 'BEN'),
    CLUB('Porto', 'POR'),
    CLUB('Braga', 'BRA'),
    CLUB('Vitoria', 'VIT'),
    CLUB('Moreirense', 'MOR'),
    CLUB('Arouca', 'ARO'),
    CLUB('Famalicao', 'FAM'),
    CLUB('Farense', 'FAR'),
    CLUB('Rio Ave', 'RA'),
    CLUB('Casa Pia', 'CAS'),
    CLUB('Gil Vicente', 'GIL'),
    CLUB('Estoril Praia', 'EST'),
    CLUB('Boavista', 'BOA'),
    CLUB('Estrela Amadora', 'EST'),
    CLUB('Portimonese', 'POR'),
    CLUB('Chaves', 'CHA'),
    CLUB('Vizela', 'VIZ')
]
POR2 = [
    CLUB('Santa Clara', 'SC'),
    CLUB('Nacional', 'NAC'),
    CLUB('AVS', 'AVS'),
    CLUB('Maritimo', 'MAR'),
    CLUB('Pacos Ferreira', 'PAC'),
    CLUB('Tondela', 'TON'),
    CLUB('Porto B', 'POR-B'),
    CLUB('Torreense', 'TOR'),
    CLUB('Mafra', 'MAF'),
    CLUB('Academico de Viseu', 'VIS'),
    CLUB('UD Leiria', 'LEI'),
    CLUB('Benfica B', 'BEN-B'),
    CLUB('Penafiel', 'PEN'),
    CLUB('Oliveirense', 'OLI'),
    CLUB('Leixoes', 'LEI'),
    CLUB('Feirenses', 'FEI'),
    CLUB('Belenenses', 'BEL'),
    CLUB('Vilaverdense', 'VIL')
]
PORTUGAL = ASSOCIATION('Portugal', 'POR', leagues = [POR1, POR2], relSpots = [3], lastSpot = 'GER')
## TIER C----
# NETHERLANDS
NED1 = [
    CLUB('PSV Eindhoven', 'PSV'),
    CLUB('Feyenoord', 'FEY'),
    CLUB('Twente', 'TWE'),
    CLUB('AZ Alkmaar', 'AZ'),
    CLUB('Ajax', 'AJX'),
    CLUB('Utrecht', 'UTR'),
    CLUB('NEC', 'NEC'),
    CLUB('Go Ahead Eagles', 'GAE'),
    CLUB('Sparta Rotterdam', 'ROT'),
    CLUB('Heerenveen', 'HEE'),
    CLUB('Fortuna Sittard', 'SIT'),
    CLUB('PEC Zwolle', 'ZWO'),
    CLUB('Almere', 'ALM'),
    CLUB('Heracles', 'HER'),
    CLUB('RKC Waalwijk', 'WAA'),
    CLUB('Excelsior', 'XL'),
    CLUB('FC Volendam', 'VOL'),
    CLUB('Vitesse', 'VIT')
]
NED2 = [
    CLUB('Willem II', 'WIL'),
    CLUB('Roda', 'ROD'),
    CLUB('Groningen', 'GRO'),
    CLUB('Dordrecht', 'DOR'),
    CLUB('Den Haag', 'DEN'),
    CLUB('De Graafschap', 'GRA'),
    CLUB('NAC', 'NAC'),
    CLUB('FC Emmen', 'EMM'),
    CLUB('MVV', 'MVV'),
    CLUB('AZ Alkmaar B', 'AZ-B'),
    CLUB('Helmond Sport', 'HEL'),
    CLUB('VVV', 'VVV'),
    CLUB('Cambuur', 'CAM'),
    CLUB('Ajax B', 'AJX'),
    CLUB('FC Eindhoven', 'EIN'),
    CLUB('PSV Eindhoven B', 'PSV-B'),
    CLUB('Telstar', 'TEL'),
    CLUB('Den Bosch', 'DB'),
    CLUB('TOP Oss', 'OSS'),
    CLUB('Utrecht B', 'UTR-B')
]
NETHERLANDS = ASSOCIATION('Netherlands', 'NED', leagues = [NED1, NED2], relSpots = [3], lastSpot = 'GER')
# Also weirdass promotion playoffs I refuse to acknowledge
# SCOTLAND
SCO1 = [
    CLUB('Celtic', 'CEL'),
    CLUB('Rangers', 'RAN'),
    CLUB('Hearts', 'HEA'),
    CLUB('Kilmarnock', 'KIL'),
    CLUB('St Mirren', 'StM'),
    CLUB('Dundee United', 'DUN'),
    CLUB('Hibernian', 'HIB'),
    CLUB('Aberdeen', 'ABE'),
    CLUB('Motherwell', 'MOT'),
    CLUB('Ross County', 'ROS'),
    CLUB('St Johnstone', 'StJ'),
    CLUB('Livingston', 'LIV')
]
SCOTLAND = ASSOCIATION('Scotland', 'SCO', leagues = [SCO1], relSpots = [], lastSpot = 'na')
# Yeah yeah I know
# GREECE
GRE1 = [
    CLUB('PAOK', 'PAOK'),
    CLUB('AEK Athens', 'AEK'),
    CLUB('Olympiacos', 'OLY'),
    CLUB('Panathinaikos', 'PAN'),
    CLUB('Aris', 'ARI'),
    CLUB('Lamia', 'LAM'),
    CLUB('Asteras Tripolis', 'AST'),
    CLUB('Atromitos', 'ATR'),
    CLUB('Panserraikos', 'PNS'),
    CLUB('OFI', 'OFI'),
    CLUB('Kifisia', 'KIF'),
    CLUB('Panetolikos', 'PNT'),
    CLUB('Volos', 'VOL'),
    CLUB('Giannina', 'GIA')
]
GREECE = ASSOCIATION('Greece', 'GRE', leagues = [GRE1], relSpots = [], lastSpot = 'na')
# Yeah yeah I know
# TURKEY
TUR1 = [
    CLUB('Galatasaray', 'GAL'),
    CLUB('Fenerbahce', 'FEN'),
    CLUB('Trabzonspor', 'TRA'),
    CLUB('Basaksehir', 'BAS'),
    CLUB('Besiktas', 'BES'),
    CLUB('Kasimpasa', 'KAS'),
    CLUB('Alanyaspor', 'ALA'),
    CLUB('Rizespor', 'RIZ'),
    CLUB('Sivasspor', 'SIV'),
    CLUB('Antalyaspor', 'ANT'),
    CLUB('Adana Demirspor', 'ADA'),
    CLUB('Samsunspor', 'SAM'),
    CLUB('Kayserispor', 'KAY'),
    CLUB('Ankaragucu', 'ANK'),
    CLUB('Karagumruk', 'KAR'),
    CLUB('Konyaspor', 'KON'),
    CLUB('Gaziantep', 'GAZ'),
    CLUB('Hatayspor', 'HAT'),
    CLUB('Pendikspor', 'PEN'),
    CLUB('Istanbulspor', 'IST')
]
TURKIYE = ASSOCIATION('Turkiye', 'TUR', leagues = [TUR1], relSpots = [], lastSpot = 'na')
# BELGIUM
BEL1 = [
    CLUB('Union SG', 'USG'),
    CLUB('Anderlecht', 'AND'),
    CLUB('Antwerp', 'ANT'),
    CLUB('Club Brugge', 'ClB'),
    CLUB('Cercle Brugge', 'CeB'),
    CLUB('Genk', 'GNK'),
    CLUB('Gent', 'GNT'),
    CLUB('Mechelen', 'MEC'),
    CLUB('Sint-Truiden', 'StT'),
    CLUB('Standard Liege', 'LIE'),
    CLUB('Westerlo', 'WES'),
    CLUB('OH Leuven', 'LEU'),
    CLUB('Charleroi', 'CHA'),
    CLUB('Eupen', 'EUP'),
    CLUB('Kortrijk', 'KOR'),
    CLUB('RWD Molenbeek', 'RWD')
]
BELGIUM = ASSOCIATION('Belgium', 'BEL', leagues = [BEL1], relSpots = [], lastSpot = 'na')
# DENMARK
DEN1 = [
    CLUB('Midtjylland', 'MID'),
    CLUB('Brondby', 'BRO'),
    CLUB('Copenhagen', 'COP'),
    CLUB('Nordsjaelland', 'NOR'),
    CLUB('AGF', 'AGF'),
    CLUB('Silkeborg', 'SIL'),
    CLUB('OB', 'OB'),
    CLUB('Lyngby', 'Lyngby'),
    CLUB('Viborg', 'Viborg'),
    CLUB('Randers', 'Randers'),
    CLUB('Vejle BK', 'VEJ'),
    CLUB('Hvidovre', 'HVI')
]
DENMARK = ASSOCIATION('Denmark', 'DEN', leagues = [DEN1], relSpots = [], lastSpot = 'na')
# SWITZERLAND
SUI1 = [
    CLUB('Young Boys', 'YB'),
    CLUB('Lugano', 'LUG'),
    CLUB('Servette', 'SER'),
    CLUB('St. Gallen', 'StG'),
    CLUB('Winterthur', 'WIN'),
    CLUB('FC Zurich', 'ZUR'),
    CLUB('Luzern', 'LUZ'),
    CLUB('Lausanne', 'LAU'),
    CLUB('Basel', 'BAS'),
    CLUB('Yverdon', 'YVE'),
    CLUB('Grasshoppers', 'GRA'),
    CLUB('Stade Lausanne-Ouchy', 'SLO')
]
SWITZERLAND = ASSOCIATION('Switzerland', 'SUI', leagues = [SUI1], relSpots = [], lastSpot = 'na')
# AUSTRIA
AUS1 = [
    CLUB('RB Salzburg', 'SAL'),
    CLUB('SK Sturm Graz', 'STU'),
    CLUB('LASK', 'LAS'),
    CLUB('Austria Klagenfurt', 'KLA'),
    CLUB('Hartberg', 'HAR'),
    CLUB('Rapid Wien', 'RAP'),
    CLUB('Austria Wien', 'AUS'),
    CLUB('Wolfsberg', 'WOL'),
    CLUB('Altach', 'ALT'),
    CLUB('Blau-Weis Linz', 'BWL'),
    CLUB('WSG Tirol', 'TIR'),
    CLUB('Austria Lustenau', 'LUS')
]
AUSTRIA = ASSOCIATION('Austria', 'AUS', leagues = [AUS1], relSpots = [], lastSpot = 'na')
# CROATIA
CRO1 = [
    CLUB('Dinamo Zagreb', 'ZAG'),
    CLUB('Rijeka', 'RIJ'),
    CLUB('Hajduk Split', 'HAJ'),
    CLUB('Osijek', 'OSI'),
    CLUB('NK Lokomotiva', 'LOK'),
    CLUB('Varazdin', 'VAR'),
    CLUB('Istra 1961', 'IST'),
    CLUB('HNK Gorica', 'GOR'),
    CLUB('Slaven Belupo', 'BEL'),
    CLUB('Rudes', 'RUD')
]
CROATIA = ASSOCIATION('Croatia', 'CRO', leagues = [CRO1], relSpots = [], lastSpot = 'na')
# CZECHIA
CZE1 = [
    CLUB('Sparta Praha', 'SPA'),
    CLUB('Slavia Praha', 'SLA'),
    CLUB('Viktoria Plzen', 'VIK'),
    CLUB('Banik', 'BAN'),
    CLUB('Mlada Boleslav', 'MLA'),
    CLUB('Slovacko', 'SLO'),
    CLUB('Liberec', 'LIB'),
    CLUB('Sigma', 'SIG'),
    CLUB('Hradec Kralove', 'HK'),
    CLUB('Teplice', 'TEP'),
    CLUB('Bohemians ___', 'BOH'),
    CLUB('Jablonec', 'JAB'),
    CLUB('FK Pardubice', 'PAR'),
    CLUB('Karvina', 'KAR'),
    CLUB('Zlin', 'ZLI'),
    CLUB('SK Dynamo', 'DYN')
]
CZECHIA = ASSOCIATION('Czechia', 'CZE', leagues = [CZE1], relSpots = [], lastSpot = 'na')




