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
readOutput <- function(){
  rm(list = ls(envir = .GlobalEnv)[ls(envir = .GlobalEnv) %>% as.list() %>% lapply(function(x){get(x) %>% class()}) %>% unlist() != 'function'],
     envir = .GlobalEnv)
  for (file in list.files('Output')){
    print(file)
    name <- strsplit(file, '[.]')[[1]][1]
    assign(name, read.csv(paste0('Output/', file)), envir = .GlobalEnv)
  }
  WinnersWide <<- Winners %>% pivot_wider(names_from = 'Year', values_from = 'Team')
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

readOutput()
