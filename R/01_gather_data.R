#' ---
#' title: Gathering Raw Data
#' author: Yuxiao Li
#' date: "`r Sys.Date()`"
#' output: github_document
#' ---

#' Here we're assembling the raw data from the three
#' datasets we want to use (RaindataPerepoch, RaindataPerehour, and coord) 
#' from various repositories on the web, and collecting
#' them in data/.
start_time <- Sys.time()

library(here)
library(downloader)

#' Set up the data directory if it doesn't exist

if (!dir.exists(here("data"))) {
  cat("creating data/ directory\n")
  dir.create(here("data"))
}
rain1_url  <- 
    "https://ndownloader.figshare.com/files/10938740"
rain1_data_file  <- "RaindataPerhour.csv"

rain2_url <- 
  "https://ndownloader.figshare.com/files/10938737"
rain2_data_file <-
  "RaindataPerepoch.csv"

## download(rain1_url, 
##        destfile = here("data", rain1_data_file),
##        mode = "wb")

coord_url <- 
  "https://ndownloader.figshare.com/files/10938746?private_link=2a4f6e9acddac309cbe9"
coord_data_file <- "coords.csv" 



## download(rain2_url, 
##        destfile = here("data", rain2_data_file),
##        mode = "wb")

## download(coord_url, 
##        destfile = here("data", coord_data_file),
##        mode = "wb")

#' 
#' Loop through all of the above, and acquire
#' files we don't have yet
#' 

url_list <- 
  c(rain1_url,
    rain2_url,
    coord_url)

data_file_list <-
  c(rain1_data_file,
    rain2_data_file,
    coord_data_file)

for(i1 in 1:length(data_file_list)){
  
  if(!file.exists(here("data", data_file_list[i1]))){
    cat("downloading ", data_file_list[i1], "\n")

    download(url_list[i1], 
             destfile = here("data", data_file_list[i1]),
             mode = "wb")
  }
}

end_time <- Sys.time()

runtime_01 <- end_time-start_time

##Running Time
runtime_01