library(plyr)
df = read.csv('colors.csv', header = FALSE)
terms = as.data.frame(df[,1])
spTerms = c()
ndf = data.frame(3,2,1)
colors = c()
colnames(ndf) = c('Color', 'CVotes', 'TVotes')

for (i in 1:nrow(df)) {
  
  temp = toString(terms[i,])
  temp = as.data.frame(strsplit(temp, '--'))
  
  spTerms = append(spTerms, toString(temp[1,1]))
  spTerms = append(spTerms, toString(temp[2,1]))
  
  spCol = toString(df[i,2])  
  colors = append(colors, toString(as.data.frame(strsplit(spCol, '='))[2,1]))
}

totalColors = append(colors,colors)

ndf = data.frame(spTerms, totalColors)
ndf = arrange(ndf,spTerms)

# text = read.delim('pledge.txt', sep = ' ', header = FALSE, colClasses = 'character')
text = paste(readLines("hell.txt"), collapse=" ")
text = tolower(text)
text = gsub("[[:punct:]]", "", text)
text = as.data.frame(strsplit(text, ' '))
colorList = c()
for (i in 1:nrow(text)) {
  indx = which(ndf$spTerms == toString(text[i,1])) 
  if(length(indx) != 0) {
    for (j in 1:length(indx)) {
      colorList = append(colorList, toString(ndf$totalColors[indx][j])) 
    }
  }
}
colorList = colorList[-which(colorList == 'None')] # MAYBE REPLACE WITH WHITE INSTEAD???
# colorList = colorList[-which(colorList == 'black')]
rColorList = c()
hsvList = data.frame(rep(0,3),rep(0,3),rep(0,3))
numSlivers = 500
count = 1
for (i in seq(1, length(colorList), round(length(colorList) / numSlivers))) {
  colTab = col2rgb(colorList[i:((i+round(length(colorList) / numSlivers))-1)])
  red = mean(colTab[1,]) 
  green = mean(colTab[2,]) 
  blue = mean(colTab[3,]) 
  # hsvList[,count] = c(red,green,blue)
  rColorList = append(rColorList, rgb(red/255, green/255, blue/255))
  hsvList[,count] = rgb2hsv(red/255, green/255, blue)
  count = count + 1
}
ncolors = c()
hsvList = as.data.frame(t(hsvList))
colnames(hsvList) = c('x','y','z')
hsvList = hsvList[order(hsvList$x,hsvList$y,hsvList$z),]
hsvList = as.data.frame(t(hsvList))
for (i in 1:ncol(hsvList)) {
  hsv2 = hsvList[,i]
  ncolors = append(ncolors, rgb(hsv2[1],hsv2[2],hsv2[3]))

}

barplot(rep(1,length(rColorList)), yaxt = 'n', col = rColorList)


