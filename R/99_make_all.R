#' ---
#' title: Make All
#' author: Yuxiao Li
#' date: "`r Sys.Date()`"
#' output: github_document
#' ---

library(here)
library(rmarkdown)

if(!dir.exists(here("results"))){
  dir.create(here("results"))
}

files_in_r_to_run <- 
  c("01_gather_data.R",
    "02_describing_raw_data.Rmd",
    "03_preprocessing_data.Rmd",
    "04_estimating_parameters.Rmd",
    "05_inference_and_simulation.Rmd",
    "11_simulation_study.Rmd")

for(i1 in 1:length(files_in_r_to_run)){
  
  rmarkdown::render(here("R", files_in_r_to_run[i1]),
                    output_format = 
                      github_document(html_preview = TRUE, toc = TRUE),
                    output_dir = here("results"))
  
}

