from Competitions import *
fromSave = False
if fromSave:
	with open(f'SAVE_TEST.dill', 'rb') as f:
		ENGLAND, SPAIN, GERMANY, ITALY, \
            FRANCE, PORTUGAL, NETHERLANDS, SCOTLAND, \
            GREECE, TURKIYE, BELGIUM, DENMARK, \
            SWITZERLAND, AUSTRIA, CROATIA, CZECHIA, \
            EURO, glob, RESULTS, DIRECTORY, WINNERS = dill.load(f)
else:	
	## TIER A ----
	# ENGLAND
	ENG1 = [
		CLUB("Man City", "MNC", 90.4),
		CLUB("Arsenal", "ARS", 81.1),
		CLUB("Liverpool", "LIV", 80.3),
		CLUB("Chelsea", "CHE", 70.7),
		CLUB("Tottenham", "TOT", 68.7),
		CLUB("Aston Villa", "AST", 68.6),
		CLUB("Newcastle", "NEW", 66.8),
		CLUB("Man United", "MNU", 64.1),
		CLUB("Brighton", "BRI", 62.7),
		CLUB("Fulham", "FUL", 60.2),
		CLUB("West Ham", "WHU", 59.9),
		CLUB("Crystal Palace", "CRY", 59.7),
		CLUB("Brentford", "BRE", 59.4),
		CLUB("Bournemouth", "BOU", 59),
		CLUB("Everton", "EVE", 57.3),
		CLUB("Forest", "FOR", 56.3),
		CLUB("Leicester", "LEI", 53.9),
		CLUB("Wolves", "WOL", 53),
		CLUB("Ipswich", "IPS", 45.8),
		CLUB("Southampton", "SOU", 45.5)
	]

	ENG2 = [
		CLUB("Leeds", "LEE", 51.3),
		CLUB("Burnley", "BUR", 51.2),
		CLUB("Sheffield United", "SHE", 43.8),
		CLUB("West Brom", "WES", 43.2),
		CLUB("Norwich", "NOR", 42.6),
		CLUB("Middlesbrough", "MID", 41.8),
		CLUB("Luton", "LUT", 40.9),
		CLUB("Sunderland", "SUN", 40.4),
		CLUB("Hull", "HUL", 38.7),
		CLUB("Blackburn", "BLA", 37.8),
		CLUB("Swansea", "SWA", 37.6),
		CLUB("Bristol City", "BRI", 37.4),
		CLUB("Coventry", "COV", 36.7),
		CLUB("Millwall", "MIL", 36.5),
		CLUB("Watford", "WAT", 36.5),
		CLUB("Preston", "PRE", 35.2),
		CLUB("Stoke", "STO", 35),
		CLUB("Sheffield Weds", "SHE", 34.3),
		CLUB("Oxford", "OXF", 31.9),
		CLUB("QPR", "QPR", 31.7),
		CLUB("Derby", "DER", 31.3),
		CLUB("Cardiff", "CAR", 31.3),
		CLUB("Plymouth", "PLY", 30.8),
		CLUB("Portsmouth", "POR", 28.1)
	]
	ENGLAND = ASSOCIATION('England', 'ENG', leagues=[ENG1, ENG2], relSpots=[3], lastSpot='ENG', DIRECTORY=DIRECTORY)
	# SPAIN
	ESP1 = [
		CLUB("Real Madrid", "REA", 82.1),
		CLUB("Barcelona", "BAR", 75.1),
		CLUB("Atletico", "ATL", 66.2),
		CLUB("Bilbao", "BIL", 62.2),
		CLUB("Girona", "GIR", 59.8),
		CLUB("Villarreal", "VIL", 59.8),
		CLUB("Sociedad", "SOC", 59),
		CLUB("Betis", "BET", 54.7),
		CLUB("Sevilla", "SEV", 52.5),
		CLUB("Mallorca", "MAL", 52.4),
		CLUB("Celta", "CEL", 51.5),
		CLUB("Osasuna", "OSA", 51.5),
		CLUB("Rayo Vallecano", "RAY", 49.3),
		CLUB("Valencia", "VAL", 49.1),
		CLUB("Getafe", "GET", 48.9),
		CLUB("Alaves", "ALA", 48.6),
		CLUB("Espanyol", "ESP", 46.2),
		CLUB("Valladolid", "VAL", 44.1),
		CLUB("Las Palmas", "LAS", 43.7),
		CLUB("Leganes", "LEG", 42.8)
	]
	ESP2 = [
		CLUB("Santander", "SAN", 43.4),
		CLUB("Oviedo", "OVI", 43.2),
		CLUB("Eibar", "EIB", 42.3),
		CLUB("Levante", "LEV", 42.1),
		CLUB("Granada", "GRA", 41.3),
		CLUB("Almeria", "ALM", 40.9),
		CLUB("Gijon", "GIJ", 39.7),
		CLUB("Cadiz", "CAD", 39.6),
		CLUB("Zaragoza", "ZAR", 38.8),
		CLUB("Huesca", "HUE", 37.9),
		CLUB("Elche", "ELC", 36.6),
		CLUB("Mirandes", "MIR", 35.2),
		CLUB("Albacete", "ALB", 34.9),
		CLUB("Burgos", "BUR", 34.5),
		CLUB("Castellon", "CAS", 33.2),
		CLUB("Tenerife", "TEN", 32.7),
		CLUB("Ferrol", "FER", 31.5),
		CLUB("Malaga", "MAL", 31.5),
		CLUB("Eldense", "ELD", 31.1),
		CLUB("Cartagena", "CAR", 30.9),
		CLUB("Cordoba", "COR", 29.7),
		CLUB("Depor", "DEP", 29.6)
	]
	SPAIN = ASSOCIATION('Spain', 'ESP', leagues = [ESP1, ESP2], relSpots = [3], lastSpot = 'ESP', DIRECTORY=DIRECTORY)
	# GERMANY
	GER1 = [
		CLUB("Leverkusen", "LEV", 77.2),
		CLUB("Bayern", "BAY", 75),
		CLUB("Dortmund", "DOR", 70.4),
		CLUB("RB Leipzig", "RB ", 69),
		CLUB("Stuttgart", "STU", 65.7),
		CLUB("Frankfurt", "FRA", 58.8),
		CLUB("Freiburg", "FRE", 56.4),
		CLUB("Werder", "WER", 54.9),
		CLUB("Mainz", "MAI", 54.7),
		CLUB("Union Berlin", "UNI", 54.1),
		CLUB("Hoffenheim", "HOF", 53.3),
		CLUB("Heidenheim", "HEI", 52.9),
		CLUB("Gladbach", "GLA", 51.8),
		CLUB("Wolfsburg", "WOL", 51.6),
		CLUB("Augsburg", "AUG", 48.1),
		CLUB("St Pauli", "ST ", 45.9),
		CLUB("Bochum", "BOC", 43.4),
		CLUB("Holstein", "HOL", 42.5)
	]

	GER2 = [
		CLUB("Duesseldorf", "DUE", 48.3),
		CLUB("Hamburg", "HAM", 47),
		CLUB("Koeln", "KOE", 45.1),
		CLUB("Karlsruhe", "KAR", 44),
		CLUB("Paderborn", "PAD", 39.8),
		CLUB("Hertha", "HER", 39.3),
		CLUB("Hannover", "HAN", 38.8),
		CLUB("Darmstadt", "DAR", 36.7),
		CLUB("Schalke", "SCH", 35.2),
		CLUB("Magdeburg", "MAG", 35),
		CLUB("Fuerth", "FUE", 33.7),
		CLUB("Lautern", "LAU", 33.2),
		CLUB("Elversberg", "ELV", 31.9),
		CLUB("Nuernberg", "NUE", 31.2),
		CLUB("Braunschweig", "BRA", 27.9),
		CLUB("Ulm", "ULM", 27.7),
		CLUB("Muenster", "MUE", 27.2),
		CLUB("Regensburg", "REG", 23.8)
	]
	GERMANY = ASSOCIATION('Germany', 'GER', leagues = [GER1, GER2], relSpots = [3], lastSpot = 'GER', DIRECTORY=DIRECTORY)
	# ITALY

	ITA1 = [
		CLUB("Inter", "INT", 80.6),
		CLUB("Atalanta", "ATA", 71.2),
		CLUB("Juventus", "JUV", 69.3),
		CLUB("Milan", "MIL", 67.7),
		CLUB("Lazio", "LAZ", 65.7),
		CLUB("Napoli", "NAP", 65.5),
		CLUB("Roma", "ROM", 63.7),
		CLUB("Fiorentina", "FIO", 63.2),
		CLUB("Bologna", "BOL", 60.8),
		CLUB("Torino", "TOR", 59.5),
		CLUB("Udinese", "UDI", 54.4),
		CLUB("Monza", "MON", 53.5),
		CLUB("Genoa", "GEN", 53.1),
		CLUB("Empoli", "EMP", 52.6),
		CLUB("Verona", "VER", 50.1),
		CLUB("Cagliari", "CAG", 48),
		CLUB("Lecce", "LEC", 46.6),
		CLUB("Parma", "PAR", 45.1),
		CLUB("Como", "COM", 44),
		CLUB("Venezia", "VEN", 43.6)
	]

	ITA2 = [
		CLUB("Sassuolo", "SAS", 47.2),
		CLUB("Cremonese", "CRE", 42.5),
		CLUB("Spezia", "SPE", 40.2),
		CLUB("Frosinone", "FRO", 39.9),
		CLUB("Salernitana", "SAL", 38.2),
		CLUB("Sampdoria", "SAM", 37.9),
		CLUB("Pisa", "PIS", 36.9),
		CLUB("Palermo", "PAL", 35.8),
		CLUB("Bari", "BAR", 34.7),
		CLUB("Catanzaro", "CAT", 34.5),
		CLUB("Brescia", "BRE", 34.2),
		CLUB("Suedtirol", "SUE", 33.5),
		CLUB("Cosenza", "COS", 32.9),
		CLUB("Juve Stabia", "JUV", 32.6),
		CLUB("Modena", "MOD", 31.9),
		CLUB("Reggiana", "REG", 31.5),
		CLUB("Mantova", "MAN", 30.9),
		CLUB("Cesena", "CES", 30.9),
		CLUB("Cittadella", "CIT", 30.1),
		CLUB("Carrarese", "CAR", 30)
	]
	ITALY = ASSOCIATION('Italy', 'ITA', leagues = [ITA1, ITA2], relSpots = [3], lastSpot = 'ESP', DIRECTORY=DIRECTORY)
	# Okay so italy has their own different promotion playoffs but its suuuuper weird so I'm ignoring the first round and the 14-points clear rule, then its just ESP

	## TIER B ----
	# FRANCE
	FRA1 = [
		CLUB("Paris SG", "PAR", 74.6),
		CLUB("Monaco", "MON", 66.2),
		CLUB("Lille", "LIL", 65.5),
		CLUB("Marseille", "MAR", 62.6),
		CLUB("Lens", "LEN", 59.2),
		CLUB("Lyon", "LYO", 58.9),
		CLUB("Brest", "BRE", 57.6),
		CLUB("Rennes", "REN", 56.1),
		CLUB("Nice", "NIC", 55.6),
		CLUB("Reims", "REI", 53.5),
		CLUB("Strasbourg", "STR", 50.9),
		CLUB("Toulouse", "TOU", 49.9),
		CLUB("Montpellier", "MON", 47.9),
		CLUB("Nantes", "NAN", 44.5),
		CLUB("Auxerre", "AUX", 44.2),
		CLUB("Le Havre", "LE ", 41.8),
		CLUB("Saint-Etienne", "SAI", 39.6),
		CLUB("Angers", "ANG", 37)
	]

	FRA2 = [
		CLUB("Lorient", "LOR", 45.4),
		CLUB("Metz", "MET", 41.9),
		CLUB("Paris FC", "PAR", 40.7),
		CLUB("Clermont", "CLE", 38.8),
		CLUB("Bastia", "BAS", 33.5),
		CLUB("Amiens", "AMI", 33),
		CLUB("Grenoble", "GRE", 32.4),
		CLUB("Rodez", "ROD", 32.4),
		CLUB("Annecy", "ANN", 32.4),
		CLUB("Pau", "PAU", 32.3),
		CLUB("Guingamp", "GUI", 32.1),
		CLUB("Caen", "CAE", 31.6),
		CLUB("Laval", "LAV", 31.1),
		CLUB("Dunkerque", "DUN", 28.4),
		CLUB("Ajaccio", "AJA", 27.9),
		CLUB("Troyes", "TRO", 26.8),
		CLUB("Red Star", "RED", 25),
		CLUB("Martigues", "MAR", 23.2)
	]
	FRANCE = ASSOCIATION('France', 'FRA', leagues = [FRA1, FRA2], relSpots = [3], lastSpot = 'GER', DIRECTORY=DIRECTORY)
	# France also has a weird Playoff system I'm ignoring the first round of, Germany's gets the point of it
	# PORTUGAL
	POR1 = [
		CLUB("Sporting", "SPO", 70.4),
		CLUB("Porto", "POR", 65.1),
		CLUB("Benfica", "BEN", 63),
		CLUB("Braga", "BRA", 50.2),
		CLUB("Guimaraes", "GUI", 47.4),
		CLUB("Famalicao", "FAM", 39.4),
		CLUB("Moreirense", "MOR", 37.3),
		CLUB("Arouca", "ARO", 37.1),
		CLUB("Gil Vicente", "GIL", 35),
		CLUB("Rio Ave", "RIO", 34.7),
		CLUB("Casa Pia", "CAS", 32.8),
		CLUB("Santa Clara", "SAN", 31.8),
		CLUB("Boavista", "BOA", 29.8),
		CLUB("Farense", "FAR", 28.9),
		CLUB("AVS Futebol", "AVS", 28.9),
		CLUB("Estoril", "EST", 28.7),
		CLUB("Nacional", "NAC", 27.9),
		CLUB("Estrela Amadora", "EST", 27.1)
	]
	PORTUGAL = ASSOCIATION('Portugal', 'POR', leagues = [POR1], relSpots = [], lastSpot = 'na', DIRECTORY=DIRECTORY)
	## TIER C----
	# NETHERLANDS
	NED1 = [
		CLUB("PSV", "PSV", 67.2),
		CLUB("Feyenoord", "FEY", 63.4),
		CLUB("Ajax", "AJA", 53),
		CLUB("Twente", "TWE", 48.6),
		CLUB("Alkmaar", "ALK", 46.7),
		CLUB("Utrecht", "UTR", 44.4),
		CLUB("Nijmegen", "NIJ", 39),
		CLUB("Sparta Rotterdam", "SPA", 38.5),
		CLUB("Go Ahead Eagles", "GO ", 35.3),
		CLUB("Sittard", "SIT", 30.6),
		CLUB("Heerenveen", "HEE", 30),
		CLUB("Zwolle", "ZWO", 29.2),
		CLUB("Willem II", "WIL", 26.5),
		CLUB("Heracles", "HER", 25.9),
		CLUB("Breda", "BRE", 25),
		CLUB("Groningen", "GRO", 24.9),
		CLUB("Waalwijk", "WAA", 24.7),
		CLUB("Almere", "ALM", 24.7)
	]
	NETHERLANDS = ASSOCIATION('Netherlands', 'NED', leagues = [NED1], relSpots = [], lastSpot = 'na', DIRECTORY=DIRECTORY)
	# Also weirdass promotion playoffs I refuse to acknowledge
	# SCOTLAND
	SCO1 = [
		CLUB("Celtic", "CEL", 53.9),
		CLUB("Rangers", "RAN", 47.1),
		CLUB("Aberdeen", "ABE", 29.9),
		CLUB("Hearts", "HEA", 29),
		CLUB("Kilmarnock", "KIL", 24.7),
		CLUB("Motherwell", "MOT", 22.5),
		CLUB("Hibernian", "HIB", 20.6),
		CLUB("St Mirren", "ST ", 20.1),
		CLUB("Dundee", "DUN", 17.6),
		CLUB("Dundee United", "DUN", 17.1),
		CLUB("St Johnstone", "ST ", 14.4),
		CLUB("Ross County", "ROS", 12.9)
	]
	SCOTLAND = ASSOCIATION('Scotland', 'SCO', leagues = [SCO1], relSpots = [], lastSpot = 'na', DIRECTORY=DIRECTORY)
	# Yeah yeah I know
	# GREECE
	GRE1 = [
		CLUB("Olympiakos", "OLY", 51.6),
		CLUB("PAOK", "PAO", 46.2),
		CLUB("AEK", "AEK", 44.7),
		CLUB("Panathinaikos", "PAN", 42.5),
		CLUB("Aris", "ARI", 35.6),
		CLUB("Panetolikos", "PAN", 21.4),
		CLUB("OFI", "OFI", 20.7),
		CLUB("Asteras Tripolis", "AST", 18.2),
		CLUB("Atromitos", "ATR", 17.5),
		CLUB("NFC Volos", "NFC", 17.3),
		CLUB("Panserraikos", "PAN", 15.6),
		CLUB("Lamia", "LAM", 15.4),
		CLUB("Levadeiakos", "LEV", 15.4),
		CLUB("Kalithea", "KAL", 15.2)
	]
	GREECE = ASSOCIATION('Greece', 'GRE', leagues = [GRE1], relSpots = [], lastSpot = 'na', DIRECTORY=DIRECTORY)
	# Yeah yeah I know
	# TURKEY
	TUR1 = [
		CLUB("Galatasaray", "GAL", 56.8),
		CLUB("Fenerbahce", "FEN", 55.3),
		CLUB("Besiktas", "BES", 40.5),
		CLUB("Trabzonspor", "TRA", 36.8),
		CLUB("Bueyueksehir", "BUE", 36),
		CLUB("Kasimpasa", "KAS", 31.1),
		CLUB("Alanyaspor", "ALA", 30.9),
		CLUB("Sivasspor", "SIV", 30.2),
		CLUB("Konyaspor", "KON", 29.4),
		CLUB("Samsunspor", "SAM", 29.2),
		CLUB("Antalyaspor", "ANT", 26.5),
		CLUB("Eyupspor", "EYU", 25.2),
		CLUB("Goeztepe", "GOE", 24.7),
		CLUB("Adana Demirspor", "ADA", 23.9),
		CLUB("Rizespor", "RIZ", 23.7),
		CLUB("Gaziantep FK", "GAZ", 23.6),
		CLUB("Kayseri", "KAY", 23.4),
		CLUB("Bodrum", "BOD", 22.7),
		CLUB("Hatayspor", "HAT", 20.1)
	]
	TURKIYE = ASSOCIATION('Turkiye', 'TUR', leagues = [TUR1], relSpots = [], lastSpot = 'na', DIRECTORY=DIRECTORY)
	# BELGIUM
	BEL1 = [
		CLUB("Brugge", "BRU", 54.8),
		CLUB("Gent", "GNT", 50.1),
		CLUB("St Gillis", "STG", 49.8),
		CLUB("Anderlecht", "AND", 49.8),
		CLUB("Antwerp", "ANT", 47.2),
		CLUB("Genk", "GNK", 46.6),
		CLUB("Mechelen", "MEC", 41.2),
		CLUB("Cercle Brugge", "CER", 37.6),
		CLUB("Charleroi", "CHA", 36.3),
		CLUB("St Truiden", "ST ", 35.3),
		CLUB("Leuven", "LEU", 35.1),
		CLUB("Westerlo", "WES", 34.3),
		CLUB("Standard", "STA", 33.3),
		CLUB("Dender", "DEN", 28.3),
		CLUB("Kortrijk", "KOR", 25.9),
		CLUB("Beerschot AC", "BEE", 22.1)
	]
	BELGIUM = ASSOCIATION('Belgium', 'BEL', leagues = [BEL1], relSpots = [], lastSpot = 'na', DIRECTORY=DIRECTORY)
	# DENMARK
	DEN1 = [
		CLUB("Midtjylland", "MID", 48.7),
		CLUB("FC Kobenhavn", "FC ", 48.3),
		CLUB("Nordsjaelland", "NOR", 45),
		CLUB("Brondby", "BRO", 42.5),
		CLUB("Aarhus", "AAR", 41.2),
		CLUB("Silkeborg", "SIL", 35.5),
		CLUB("Randers", "RAN", 34.2),
		CLUB("Viborg", "VIB", 32.9),
		CLUB("Lyngby", "LYN", 26.1),
		CLUB("Aalborg", "AAL", 24.3),
		CLUB("SonderjyskE", "SON", 23.8),
		CLUB("Vejle", "VEJ", 21.4)
	]
	DENMARK = ASSOCIATION('Denmark', 'DEN', leagues = [DEN1], relSpots = [], lastSpot = 'na', DIRECTORY=DIRECTORY)
	# SWITZERLAND
	SUI1 = [
		CLUB("Young Boys", "YOU", 40.4),
		CLUB("Servette", "SER", 36.4),
		CLUB("Zuerich", "ZUE", 36.1),
		CLUB("Lugano", "LUG", 35.7),
		CLUB("StGallen", "STG", 34.6),
		CLUB("Basel", "BAS", 33.3),
		CLUB("Luzern", "LUZ", 30.6),
		CLUB("Lausanne", "LAU", 25),
		CLUB("Grasshoppers", "GRA", 23.1),
		CLUB("Yverdon Sport", "YVE", 23),
		CLUB("Sion", "SIO", 22.4),
		CLUB("Winterthur", "WIN", 21.7),
		CLUB("Thun", "THU", 20.2)
	]
	SWITZERLAND = ASSOCIATION('Switzerland', 'SUI', leagues = [SUI1], relSpots = [], lastSpot = 'na', DIRECTORY=DIRECTORY)
	# AUSTRIA
	AUS1 = [
		CLUB("Salzburg", "SAL", 45.6),
		CLUB("Sturm Graz", "STU", 44.1),
		CLUB("Rapid Wien", "RAP", 38.4),
		CLUB("LASK", "LAS", 32.3),
		CLUB("Austria Wien", "AUS", 31.5),
		CLUB("Wolfsberg", "WOL", 29.2),
		CLUB("Hartberg", "HAR", 28),
		CLUB("Klagenfurt", "KLA", 25),
		CLUB("BW Linz", "BW ", 22),
		CLUB("Altach", "ALT", 19.5),
		CLUB("Wattens", "WAT", 18),
		CLUB("GAK", "GAK", 15.8)
	]
	AUSTRIA = ASSOCIATION('Austria', 'AUS', leagues = [AUS1], relSpots = [], lastSpot = 'na', DIRECTORY=DIRECTORY)
	# CROATIA
	CRO1 = [
		CLUB("Dinamo Zagreb", "DIN", 45),
		CLUB("Hajduk", "HAJ", 36.1),
		CLUB("Rijeka", "RIJ", 32),
		CLUB("Osijek", "OSI", 27.8),
		CLUB("Lok Zagreb", "LOK", 23.1),
		CLUB("Varazdin", "VAR", 20.5),
		CLUB("Istra 1961", "IST", 19.8),
		CLUB("HNK Gorica", "HNK", 15.4),
		CLUB("Slaven Belupo", "SLA", 13.4),
		CLUB("Sibenik", "SIB", 10)
	]
	CROATIA = ASSOCIATION('Croatia', 'CRO', leagues = [CRO1], relSpots = [], lastSpot = 'na', DIRECTORY=DIRECTORY)
	# CZECHIA
	CZE1 = [
		CLUB("Slavia Praha", "SLA", 61),
		CLUB("Sparta Praha", "SPA", 57.4),
		CLUB("Viktoria Plzen", "VIK", 48.4),
		CLUB("Banik Ostrava", "BAN", 35),
		CLUB("Jablonec", "JAB", 31.9),
		CLUB("Mlada Boleslav", "MLA", 31.5),
		CLUB("Slovacko", "SLO", 31.2),
		CLUB("Hradec Kralove", "HRA", 30.7),
		CLUB("Sigma Olomouc", "SIG", 29.9),
		CLUB("Slovan Liberec", "SLO", 28),
		CLUB("Bohemians Praha", "BOH", 27.5),
		CLUB("Teplice", "TEP", 24.9),
		CLUB("Pardubice", "PAR", 23.6),
		CLUB("Karvina", "KAR", 21.6),
		CLUB("Dukla", "DUK", 18),
		CLUB("Ceske Budejovice", "CES", 14.7)
	]
	CZECHIA = ASSOCIATION('Czechia', 'CZE', leagues = [CZE1], relSpots = [], lastSpot = 'na', DIRECTORY=DIRECTORY)



