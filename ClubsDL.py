from CompetitionsDL import *
fromSave = False #'TEST_DL'
if fromSave:
	with open(f'SAVE_{fromSave}.dill', 'rb') as f:
		DreamLeague, RESULTS, DIRECTORY, WINNERS = dill.load(f)
else:
    Division1 = [
        CLUB("Man City", "MAN", 84.4), # 90.4, but they keep losing
        CLUB("Real Madrid", "REA", 82.1),
        CLUB("Arsenal", "ARS", 81.1),
        CLUB("Inter", "INT", 80.6),
        CLUB("Liverpool", "LIV", 80.3),
        CLUB("Leverkusen", "LEV", 77.2),
        CLUB("Barcelona", "BAR", 75.1),
        CLUB("Bayern", "BAY", 75),
        CLUB("Paris SG", "PAR", 74.6),
        CLUB("Atalanta", "ATA", 71.2),
        CLUB("Chelsea", "CHE", 70.7),
        CLUB("Dortmund", "DOR", 70.4),
        CLUB("Sporting", "SPO", 70.4),
        CLUB("Juventus", "JUV", 69.3),
        CLUB("RB Leipzig", "RB ", 69),
        CLUB("Tottenham", "TOT", 68.7)
    ]

    Division2 = [
        CLUB("Aston Villa", "AST", 68.6),
        CLUB("Milan", "MIL", 67.7),
        CLUB("PSV", "PSV", 67.2),
        CLUB("Newcastle", "NEW", 66.8),
        CLUB("Atletico", "ATL", 66.2),
        CLUB("Monaco", "MON", 66.2),
        CLUB("Stuttgart", "STU", 65.7),
        CLUB("Lazio", "LAZ", 65.7),
        CLUB("Napoli", "NAP", 65.5),
        CLUB("Lille", "LIL", 65.5),
        CLUB("Porto", "POR", 65.1),
        CLUB("Man United", "MAN", 64.1),
        CLUB("Roma", "ROM", 63.7),
        CLUB("Feyenoord", "FEY", 63.4),
        CLUB("Fiorentina", "FIO", 63.2),
        CLUB("Benfica", "BEN", 63)
    ]

    Division3 = [
        CLUB("Brighton", "BRI", 62.7),
        CLUB("Marseille", "MAR", 62.6),
        CLUB("Bilbao", "BIL", 62.2),
        CLUB("Slavia Praha", "SLA", 61),
        CLUB("Bologna", "BOL", 60.8),
        CLUB("Fulham", "FUL", 60.2),
        CLUB("West Ham", "WES", 59.9),
        CLUB("Torino", "TOR", 59.8),
        CLUB("Girona", "GIR", 59.8),
        CLUB("Villarreal", "VIL", 59.8),
        CLUB("Crystal Palace", "CRY", 59.7),
        CLUB("Brentford", "BRE", 59.4),
        CLUB("Lens", "LEN", 59.2),
        CLUB("Sociedad", "SOC", 59),
        CLUB("Bournemouth", "BOU", 59),
        CLUB("Lyon", "LYO", 58.9)
    ]

    Division4 = [
        CLUB("Frankfurt", "FRA", 58.9),
        CLUB("Brest", "BRE", 57.6),
        CLUB("Forest", "FOR", 57.5),
        CLUB("Sparta Praha", "SPA", 57.4),
        CLUB("Everton", "EVE", 57.3),
        CLUB("Galatasaray", "GAL", 56.8),
        CLUB("Rennes", "REN", 56.4),
        CLUB("Freiburg", "FRE", 56.4),
        CLUB("Nice", "NIC", 55.6),
        CLUB("Fenerbahce", "FEN", 55.3),
        CLUB("Udinese", "UDI", 55.1),
        CLUB("Werder", "WER", 54.9),
        CLUB("Brugge", "BRU", 54.8),
        CLUB("Betis", "BET", 54.7),
        CLUB("Mainz", "MAI", 54.5),
        CLUB("Union Berlin", "UNI", 54.1)
    ]

    Division5 = [
        CLUB("Celtic", "CEL", 53.9),
        CLUB("Sevilla", "SEV", 53.6),
        CLUB("Monza", "MON", 53.5),
        CLUB("Reims", "REI", 53.5),
        CLUB("Hoffenheim", "HOF", 53.3),
        CLUB("Genoa", "GEN", 53.1),
        CLUB("Zenit", "ZEN", 53.1),
        CLUB("Ajax", "AJA", 53),
        CLUB("Wolves", "WOL", 53),
        CLUB("Heidenheim", "HEI", 52.9),
        CLUB("Leicester", "LEI", 52.8),
        CLUB("Empoli", "EMP", 52.6),
        CLUB("Mallorca", "MAL", 52.4),
        CLUB("Gladbach", "GLA", 52),
        CLUB("Wolfsburg", "WOL", 51.6),
        CLUB("Olympiakos", "OLY", 51.6)
    ]

    Division6 = [
        CLUB("Celta", "CEL", 51.5),
        CLUB("Osasuna", "OSA", 51.5),
        CLUB("Leeds", "LEE", 51.3),
        CLUB("Burnley", "BUR", 51.2),
        CLUB("Strasbourg", "STR", 50.9),
        CLUB("Braga", "BRA", 50.2),
        CLUB("Gent", "GEN", 50.1),
        CLUB("Verona", "VER", 50.1),
        CLUB("Toulouse", "TOU", 49.9),
        CLUB("St Gillis", "ST ", 49.8),
        CLUB("Anderlecht", "AND", 49.8),
        CLUB("Bodoe Glimt", "BOD", 49.4),
        CLUB("Rayo Vallecano", "RAY", 49.3),
        CLUB("Valencia", "VAL", 49.1),
        CLUB("FC Krasnodar", "FC ", 49),
        CLUB("Getafe", "GET", 48.9)
    ]

    Division7 = [
        CLUB("Midtjylland", "MID", 48.7),
        CLUB("Twente", "TWE", 48.6),
        CLUB("Alaves", "ALA", 48.6),
        CLUB("Viktoria Plzen", "VIK", 48.4),
        CLUB("FC Kobenhavn", "FC ", 48.3),
        CLUB("Duesseldorf", "DUE", 48.3),
        CLUB("Augsburg", "AUG", 48.2),
        CLUB("Montpellier", "MON", 47.9),
        CLUB("Guimaraes", "GUI", 47.4),
        CLUB("Cagliari", "CAG", 47.4),
        CLUB("Sassuolo", "SAS", 47.2),
        CLUB("Antwerp", "ANT", 47.2),
        CLUB("Rangers", "RAN", 47.1),
        CLUB("Hamburg", "HAM", 47),
        CLUB("Alkmaar", "ALK", 46.7),
        CLUB("Lecce", "LEC", 46.6)
    ]

    Division8 = [
        CLUB("Genk", "GEN", 46.6),
        CLUB("PAOK", "PAO", 46.2),
        CLUB("St Pauli", "ST ", 45.9),
        CLUB("Ipswich", "IPS", 45.8),
        CLUB("Salzburg", "SAL", 45.6),
        CLUB("Southampton", "SOU", 45.5),
        CLUB("Espanyol", "ESP", 45.2),
        CLUB("Parma", "PAR", 45.1),
        CLUB("Lorient", "LOR", 45.1),
        CLUB("Nordsjaelland", "NOR", 45),
        CLUB("Dinamo Zagreb", "DIN", 45),
        CLUB("CSKA Moskva", "CSK", 44.9),
        CLUB("AEK", "AEK", 44.7),
        CLUB("Shakhtar", "SHA", 44.6),
        CLUB("Nantes", "NAN", 44.5),
        CLUB("Utrecht", "UTR", 44.4)
    ]

    Division9 = [
        CLUB("Lok Moskva", "LOK", 44.4),
        CLUB("Auxerre", "AUX", 44.2),
        CLUB("Koeln", "KOE", 44.1),
        CLUB("Sturm Graz", "STU", 44.1),
        CLUB("Valladolid", "VAL", 44.1),
        CLUB("Karlsruhe", "KAR", 44),
        CLUB("Sheffield United", "SHE", 43.8),
        CLUB("Las Palmas", "LAS", 43.7),
        CLUB("Como", "COM", 43.7),
        CLUB("Venezia", "VEN", 43.6),
        CLUB("Crvena Zvezda", "CRV", 43.5),
        CLUB("Santander", "SAN", 43.4),
        CLUB("Bochum", "BOC", 43.4),
        CLUB("M Tel Aviv", "M T", 43.3),
        CLUB("West Brom", "WES", 43.2),
        CLUB("Oviedo", "OVI", 43.2)
    ]

    Division10 = [
        CLUB("Dynamo Moskva", "DYN", 43),
        CLUB("Leganes", "LEG", 42.8),
        CLUB("Norwich", "NOR", 42.7),
        CLUB("Panathinaikos", "PAN", 42.5),
        CLUB("Brondby", "BRO", 42.5),
        CLUB("Cremonese", "CRE", 42.5),
        CLUB("Holstein", "HOL", 42.5),
        CLUB("Maccabi Haifa", "MAC", 42.3),
        CLUB("Metz", "MET", 42.3),
        CLUB("Eibar", "EIB", 42.3),
        CLUB("Levante", "LEV", 42.1),
        CLUB("Middlesbrough", "MID", 41.8),
        CLUB("Molde", "MOL", 41.8),
        CLUB("Dynamo Kyiv", "DYN", 41.5),
        CLUB("Le Havre", "LE ", 41.5),
        CLUB("Granada", "GRA", 41.3)
    ]

    Division11 = [
        CLUB("Mechelen", "MEC", 41.2),
        CLUB("Karabakh Agdam", "KAR", 41.2),
        CLUB("Aarhus", "AAR", 41.2),
        CLUB("Almeria", "ALM", 40.9),
        CLUB("Spartak Moskva", "SPA", 40.9),
        CLUB("Luton", "LUT", 40.9),
        CLUB("Paderborn", "PAD", 40.7),
        CLUB("Paris FC", "PAR", 40.7),
        CLUB("Besiktas", "BES", 40.5),
        CLUB("Young Boys", "YOU", 40.4),
        CLUB("Sunderland", "SUN", 40.4),
        CLUB("Malmoe", "MAL", 40.2),
        CLUB("Legia", "LEG", 40),
        CLUB("Spezia", "SPE", 39.9),
        CLUB("Frosinone", "FRO", 39.9),
        CLUB("Gijon", "GIJ", 39.7)
    ]

    Division12 = [
        CLUB("Lech", "LEC", 39.7),
        CLUB("Cadiz", "CAD", 39.6),
        CLUB("Saint-Etienne", "SAI", 39.6),
        CLUB("Famalicao", "FAM", 39.4),
        CLUB("Hertha", "HER", 39.3),
        CLUB("Rakow", "RAK", 39.2),
        CLUB("Hannover", "HAN", 38.8),
        CLUB("Razgrad", "RAZ", 38.8),
        CLUB("Zaragoza", "ZAR", 38.8),
        CLUB("Hull", "HUL", 38.7),
        CLUB("Sparta Rotterdam", "SPA", 38.5),
        CLUB("Rapid Wien", "RAP", 38.4),
        CLUB("Brann", "BRA", 38.3),
        CLUB("Salernitana", "SAL", 38.2),
        CLUB("Nijmegen", "NIJ", 38),
        CLUB("Huesca", "HUE", 37.9)
    ]

    Division13 = [
        CLUB("Sampdoria", "SAM", 37.9),
        CLUB("Blackburn", "BLA", 37.8),
        CLUB("Swansea", "SWA", 37.6),
        CLUB("Cercle Brugge", "CER", 37.6),
        CLUB("Clermont", "CLE", 37.5),
        CLUB("Bristol City", "BRI", 37.4),
        CLUB("Moreirense", "MOR", 37.3),
        CLUB("Ferencvaros", "FER", 37.3),
        CLUB("Arouca", "ARO", 37.1),
        CLUB("Angers", "ANG", 37),
        CLUB("Trabzonspor", "TRA", 37),
        CLUB("Pisa", "PIS", 36.9),
        CLUB("Elfsborg", "ELF", 36.9),
        CLUB("Coventry", "COV", 36.7),
        CLUB("Darmstadt", "DAR", 36.7),
        CLUB("Elche", "ELC", 36.6)
    ]

    Division14 = [
        CLUB("Millwall", "MIL", 36.5),
        CLUB("Watford", "WAT", 36.5),
        CLUB("Servette", "SER", 36.4),
        CLUB("Jagiellonia", "JAG", 36.4),
        CLUB("Charleroi", "CHA", 36.3),
        CLUB("Hajduk", "HAJ", 36.1),
        CLUB("Zuerich", "ZUE", 36.1),
        CLUB("Bueyueksehir", "BUE", 36),
        CLUB("Palermo", "PAL", 35.8),
        CLUB("Lugano", "LUG", 35.7),
        CLUB("Aris", "ARI", 35.6),
        CLUB("Hammarby", "HAM", 35.4),
        CLUB("Go Ahead Eagles", "GO ", 35.3),
        CLUB("St Truiden", "ST ", 35.3),
        CLUB("Preston", "PRE", 35.2),
        CLUB("Mirandes", "MIR", 35.2)
    ]

    Division15 = [
        CLUB("Schalke", "SCH", 35.2),
        CLUB("Leuven", "LEU", 35.1),
        CLUB("Silkeborg", "SIL", 35.1),
        CLUB("Sheffield Weds", "SHE", 35.1),
        CLUB("Stoke", "STO", 35),
        CLUB("Viking", "VIK", 35),
        CLUB("Banik Ostrava", "BAN", 35),
        CLUB("Bari", "BAR", 35),
        CLUB("Magdeburg", "MAG", 35),
        CLUB("Albacete", "ALB", 34.9),
        CLUB("Pogon", "POG", 34.9),
        CLUB("Rio Ave", "RIO", 34.7),
        CLUB("StGallen", "STG", 34.6),
        CLUB("Burgos", "BUR", 34.5),
        CLUB("Catanzaro", "CAT", 34.5),
        CLUB("Gil Vicente", "GIL", 34.3)
    ]

    Division16 = [
        CLUB("Westerlo", "WES", 34.3),
        CLUB("Brescia", "BRE", 34.2),
        CLUB("Randers", "RAN", 34.2),
        CLUB("Amiens", "AMI", 34.1),
        CLUB("Steaua", "STE", 33.8),
        CLUB("Fuerth", "FUE", 33.7),
        CLUB("Bastia", "BAS", 33.5),
        CLUB("Rostov", "ROS", 33.5),
        CLUB("Suedtirol", "SUE", 33.5),
        CLUB("Casa Pia", "CAS", 33.3),
        CLUB("Standard", "STA", 33.3),
        CLUB("Castellon", "CAS", 33.2),
        CLUB("Basel", "BAS", 33.2),
        CLUB("Annecy", "ANN", 33.2),
        CLUB("Lautern", "LAU", 33.2),
        #CLUB("Viborg", "VIB", 32.9)
		CLUB("HydroHomies", "H20", 30)
    ]
	
    DreamLeague = DL_ASSOCIATION('Dream League', 'DL', 
							  [Division1, Division2, Division3, Division4,
		                        Division5, Division6, Division7, Division8,
								Division9, Division10, Division11, Division12,
								Division13, Division14, Division15, Division16],
							   DIRECTORY=DIRECTORY)

