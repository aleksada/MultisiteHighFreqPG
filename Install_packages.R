#' ---
#' title: Install Packages
#' author: Yuxiao Li
#' date: "`r Sys.Date()`"
#' output: github_document
#' ---

if(require(Rmarkdown) == FALSE) 
    install.packages("Rmarkdown")
if(require(here) == FALSE) 
    install.packages("here")
if(require(downloader) == FALSE) 
    install.packages("downloader")
if(require(readr) == FALSE) 
    install.packages("readr")
if(require(reshape2) == FALSE) 
    install.packages("reshape2")
if(require(ggplot2) == FALSE) 
    install.packages("ggplot2")
if(require(dplyr) == FALSE) 
    install.packages("dplyr")
if(require(sn) == FALSE) 
    install.packages("sn")
if(require(geoR) == FALSE) 
    install.packages("geoR")
if(require(cowplot) == FALSE) 
    install.packages("cowplot")