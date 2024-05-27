library(tidyverse)
`%like%` <- function(x, y){return((1:length(x)) %in% do.call(c, lapply(y, grep, x=x)))}
`%notlike%` <- function(x, y){return(!((1:length(x)) %in% do.call(c, lapply(y, grep, x=x))))}
groupr <- function(df, newname, col, tests, vals = NULL, catchall = F){  
  if(nrow(df)==0){    
    warning('Empty df in groupr')    
    return(df)  
  }  
  if(is_null(vals)){vals <- tests}  
  vec <- df[[col]]  
  len <- length(vec)  
  g <- lapply(tests, grep, x=vec)  
  out <- if(isFALSE(catchall)){vec} else {rep(catchall, len)}  
  for (ind in length(g):1){ out[g[[ind]]] <- vals[ind] }  
  df[[newname]] <- out  
  return(df)
}
setwd('/Users/yungzig/Desktop/CSProjects/Soccer/SoccerManager')
clearOutput <- function(){unlink('Output/*')}
EUROreformPI <- function(){
  ChampsLeaguePlayin <<- do.call(rbind, ls(envir = .GlobalEnv)[ls(envir = .GlobalEnv) %like% 'CLP'] %>% as.list() %>% 
                                  lapply(function(x){get(x) %>% 
                                      mutate(PATH = strsplit(strsplit(x, 'Fixtures')[[1]][1], '_')[[1]][2] %>% as.numeric())})) 
  rm(list = ls(envir = .GlobalEnv)[ls(envir = .GlobalEnv) %like% 'CLP'], envir = .GlobalEnv)
  unlink('Output/CLP_*')
  EuropaLeaguePlayin <<- do.call(rbind, ls(envir = .GlobalEnv)[ls(envir = .GlobalEnv) %like% 'ELP'] %>% as.list() %>% 
                                  lapply(function(x){get(x) %>% 
                                      mutate(PATH = strsplit(strsplit(x, 'Fixtures')[[1]][1], '_')[[1]][2] %>% as.numeric())})) 
  rm(list = ls(envir = .GlobalEnv)[ls(envir = .GlobalEnv) %like% 'ELP'], envir = .GlobalEnv)
  unlink('Output/ELP_*')
  ConfLeaguePlayin <<- do.call(rbind, ls(envir = .GlobalEnv)[ls(envir = .GlobalEnv) %like% 'ECP'] %>% as.list() %>% 
                                lapply(function(x){get(x) %>% 
                                    mutate(PATH = strsplit(strsplit(x, 'Fixtures')[[1]][1], '_')[[1]][2] %>% as.numeric())}))
  rm(list = ls(envir = .GlobalEnv)[ls(envir = .GlobalEnv) %like% 'ECP'], envir = .GlobalEnv)
  unlink('Output/ECP_*')
}
EUROreformGS <- function(){
  ChampsLeague <<- do.call(rbind, ls(envir = .GlobalEnv)[ls(envir = .GlobalEnv) %like% 'CLG'] %>% as.list() %>% 
                             lapply(function(x){get(x) %>% 
                                 mutate(GROUP = strsplit(strsplit(x, 'Standings')[[1]][1], '_')[[1]][2])})) %>%
    select(GROUP, everything())
  rm(list = ls(envir = .GlobalEnv)[ls(envir = .GlobalEnv) %like% 'CLG'], envir = .GlobalEnv)
  unlink('Output/CLG_*')
  EuropaLeague <<- do.call(rbind, ls(envir = .GlobalEnv)[ls(envir = .GlobalEnv) %like% 'ELG'] %>% as.list() %>% 
                             lapply(function(x){get(x) %>% 
                                 mutate(GROUP = strsplit(strsplit(x, 'Standings')[[1]][1], '_')[[1]][2])})) %>%
    select(GROUP, everything())
  rm(list = ls(envir = .GlobalEnv)[ls(envir = .GlobalEnv) %like% 'ELG'], envir = .GlobalEnv)
  unlink('Output/ELG_*')
  ConferenceLeague <<- do.call(rbind, ls(envir = .GlobalEnv)[ls(envir = .GlobalEnv) %like% 'ECG'] %>% as.list() %>% 
                             lapply(function(x){get(x) %>% 
                                 mutate(GROUP = strsplit(strsplit(x, 'Standings')[[1]][1], '_')[[1]][2])})) %>%
    select(GROUP, everything())
  rm(list = ls(envir = .GlobalEnv)[ls(envir = .GlobalEnv) %like% 'ECG'], envir = .GlobalEnv)
  unlink('Output/ECG_*')
}

readOutput <- function(){
  rm(list = ls(envir = .GlobalEnv)[ls(envir = .GlobalEnv) %>% as.list() %>% 
                                     lapply(function(x){get(x) %>% class()}) %>% 
                                     unlist() != 'function' & ls(envir = .GlobalEnv) %notlike% 'League'],
     envir = .GlobalEnv)
  for (file in list.files('Output')){
    print(file)
    name <- strsplit(file, '[.]')[[1]][1]
    assign(name, read.csv(paste0('Output/', file)), envir = .GlobalEnv)
  }
  WinnersWide <<- Winners %>% pivot_wider(names_from = 'Year', values_from = 'Team')
  if(ls(envir = .GlobalEnv)[ls(envir = .GlobalEnv) %like% 'CLP'] %>% length() > 0){
    EUROreformPI()
  }
  if(ls(envir = .GlobalEnv)[ls(envir = .GlobalEnv) %like% 'CLG'] %>% length() > 0){
    EUROreformGS()
  }
}
teamResults <- function(team){
  one <- Results %>% filter(Home == team | Away == team)
  keeps <- one %>% select(Year, Competition, Round, Notes)
  new <- one %>% mutate(
    Team = ifelse(Home == team, Home, Away), TeamScore = ifelse(Home == team, HomeScore, AwayScore),
    Opp = ifelse(Home == team, Away, Home), OppScore = ifelse(Home == team, AwayScore, HomeScore),
    Type = ifelse(Notes %like% c('Neutral', 'No Game'), 'Neutral', ifelse(Home == team, 'Home', 'Away'))   
  )
  new %>% select(Year, Competition, Round, Type, Team, TeamScore, OppScore, Opp, Notes)
}


clearOutput()
readOutput()
WHU <- teamResults('West Ham United')
teamResults('AFC Wimbledon')


