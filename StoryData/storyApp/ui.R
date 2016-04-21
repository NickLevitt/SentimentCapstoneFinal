#Partial Authorship by Nick Levitt
library(ggplot2)
stories = c('AnnaKarenina', 'HuckleberryFinn', 'AliceInWonderland', 'Dracula', 'Metamorphosis', 'WizardOfOz', 'WarOfWorlds','TimeMachine','JungleBook', 'CatcherInRye')
emotions = c('JOY','FEAR','ANGER','SADNESS','DISGUST','SHAME','GUILT')
# Define UI for dataset viewer application
shinyUI(navbarPage("View Story Plots", 
                   tabPanel("Plots",
                            sidebarLayout(
                              sidebarPanel(
                                selectInput("story", "Choose a Story:", 
                                            choices = stories),
                                selectizeInput("emot", "Choose emotion(s):", 
                                               choices = emotions, selected = emotions[1], multiple=TRUE),
                                
                                checkboxInput('point', 'Show Data Points?', value = FALSE),
                                checkboxInput('line', 'Show line graph?', value = FALSE)
                                # checkboxInput('log', 'Log transform?', value = FALSE)
                              ),
                              
                              mainPanel(
                                plotOutput("plot", height = 700)
                              )
                            )
                   )
  )
)
                  





                                