library(ggplot2)
library(reshape)

setwd("~/Desktop/SentimentCap/StoryData")

df = as.data.frame(read.csv('DraculaSent.csv', header = FALSE))
names = c('JOY','FEAR','ANGER','SADNESS','DISGUST','SHAME','GUILT')
col1 = c()
col2= c()
col3 = c()
for(i in 1:7) {
  for (j in 1:50) {
    col1 = append(col1, df[i,j])
    print(df[i,j])
  }
  col2 = append(col2, rep(names[i], 50))
  col3 = append(col3, seq(1,50))
}

df = data.frame(value = col1, emot = col2, time = col3)
p = ggplot(df, aes(x = time, y = value, color = factor(emot)))
p + geom_smooth(se = FALSE) + geom_point() + geom_line()


