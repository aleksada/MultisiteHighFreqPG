#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(here)
load(here("SimulateRain","estimation.cov.VAR1.RData"))
# Define UI for application that draws a histogram
ui <- fluidPage(
   
   # Application title
   titlePanel("Rainfall simulation"),
   
   # Sidebar with a slider input for number of bins 
   sidebarLayout(
      sidebarPanel(
         sliderInput("alpha",
                     "Skewness:",
                     min = -100,
                     max = 100,
                     value = 10),
         sliderInput("nu",
                     "Degree of Freedom",
                     min = 3,
                     max = 20,
                     value = 5),
         sliderInput("B",
                     "Temporal dependence",
                     min = 0,
                     max = 1,
                     value = .5)
      ),
      
      # Show a plot of the generated distribution
      mainPanel(
         plotOutput("distPlot",height = "800px")
      )
   )
)

# Define server logic required to draw a histogram
server <- function(input, output) {
   output$distPlot <- renderPlot({
       sigma <- results.VAR1$sigt[,1]
       ut<-results.VAR1$ut
           NT <- 28800
           nu <- input$nu
           alpha <- input$alpha
           bvdelta <- sqrt(nu) * gamma(1/2 * (nu - 1))/sqrt(pi)/gamma(1/2 * nu) * 
               alpha/sqrt(1 + alpha^2)
           omega <- 1/sqrt((nu/(nu-2) - bvdelta^2))
           xi<- -omega * bvdelta
           set.seed(2)
           error <- rst(NT, xi = xi, omega = omega, alpha, nu)*sigma
           y <- rep(0,NT)
           for(t in 2: NT){
               y[t] <- input$B * y[t - 1] + error[t]
               y[t] <- ifelse(y[t] > ut[t], y[t], 0)
           }
           par(mfrow=c(2,1))
           plot.ts(y,ylim=c(0,30),xlab='time')
           hist(y,xlab='time')

   })
}

# Run the application 
shinyApp(ui = ui, server = server)

