library(ggplot2)

#### Define server logic required to summarize and view the selected dataset
shinyServer(function(input, output, session) {
  output$plot <- renderPlot({
    if (length(input$emot) > 0) {
      sname = paste('../',input$story, 'Sent.csv', sep='')
      df = as.data.frame(read.csv(sname, header = FALSE))
      col1 = c()
      col2= c()
      col3 = c()
      names = c('JOY','FEAR','ANGER','SADNESS','DISGUST','SHAME','GUILT')
      for(i in 1:7) {
        for (j in 1:50) {
          col1 = append(col1, df[i,j])
        }
        col2 = append(col2, rep(names[i], 50))
        col3 = append(col3, seq(1,50))
      }
      
      df = data.frame(value = col1, emot = col2, time = col3)
      emotnames = c('JOY','FEAR','ANGER','SADNESS','DISGUST','SHAME','GUILT')
      indx = c()
      for(i in 1:length(df$emot)) {
        if(any(df$emot[i] == input$emot)) {
          indx = append(indx,i)
        }
      }
      df = df[indx,]
      
      p = ggplot(df, aes(x = time, y = value, color = factor(emot)))
      p = p + geom_smooth(se = FALSE)
      if (input$point) {
        p = p + geom_point()
      }
      if (input$line) {
        p = p + geom_line()
      }
#       if(input$log) {
#         p = p + scale_y_log10()
#       }
      p
    }
    })
})
