install.packages(c("httr", "jsonlite", 'stringdist'))
library(httr)
library(jsonlite)
library(stringdist)
res <- GET("api.clubelo.com/2024-10-26")
con <- res$content
char <- rawToChar(con)
data <- fromJSON(char)
t <- read.csv(text=char) %>% type_convert()
x <-  ((char %>% strsplit('\n'))[[1]] %>% as.list() %>% 
  lapply(function(x){strsplit(x, ',') %>% as.list() }))[1:640] %>%
  as.data.frame() %>% base::t() %>% as.data.frame()
names(x) <- x[1,] %>% as.character()
x = x[2:640,] %>% type_convert()
row.names(x) <- NULL

Using <- x %>% filter(Country %in% c('ENG', 'GER', 'ESP', 'ITA', 'FRA', 'POR',
                                     'NED', 'SCO', 'GRE', 'TUR', 'BEL', 'DEN',
                                     'SUI', 'AUT', 'CRO', 'CZE')) %>%
  mutate(ELO =  round(0.091 * Elo - 98.304, 1),
         str = paste0('CLUB("', Club, '", "', Club %>% substr(1, 3) %>% toupper(),
                      '", ', ELO, ')')) %>%
  group_by(Country, Level) %>% summarize(out = paste0(str, collapse = ',\n\t')) %>%
  mutate(str = paste0(Country, Level, ' = [\n\t', out, '\n]')) %>% arrange(Country, Level)

UsingDL <- t %>% mutate(rank = row_number()) %>% filter(rank <= 256) %>%
  mutate(ELO =  round(0.091 * Elo - 98.304, 1),
         str = paste0('CLUB("', Club, '", "', Club %>% substr(1, 3) %>% toupper(),
                      '", ', ELO, ')'),
         Division = 1+((rank-1) %/% 16)) %>% 
  group_by(Division) %>%
  summarize(out = paste0(str, collapse = ',\n\t')) %>%
  mutate(str = paste0('Division', Division, ' = [\n\t', out, '\n]'))

paste0(UsingDL$str, collapse = '\n\n') %>% write()

help <- unique(x[c('Country', 'Level')])






  
df <- do.call(rbind, (char %>% strsplit('\n'))[[1]] %>% as.list())


Clubs <- readLines('Clubs.py') %>% as.list()
ClubDF <- data.frame(ClubName = Clubs[Clubs %like% 'CLUB\\('] %>% 
                       lapply(function(x) strsplit(x, "'")[[1]][2]) %>% unlist(),
                     ABR =  Clubs[Clubs %like% 'CLUB\\('] %>% 
                       lapply(function(x) strsplit(x, "'")[[1]][4]) %>% unlist())
ELO <- NULL
for (i in 1:nrow(ClubDF)){
  #i <- 2
  temp = (ClubDF[i,] %>% mutate(help = 1) %>% 
    left_join(x %>% select(Club, Elo) %>% mutate(help = 1)) %>%
    mutate(Score = stringsim(ClubName, Club)) %>% arrange(-Score))[1,]
  ELO <- rbind(ELO, temp)
}
\