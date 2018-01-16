library('tidyverse')
country <- read.csv('processed_countries_1.csv')
Nobel <- read.csv('NobelPrize1830-2000-NULL-v2.csv')

Nobel$birthYear <- as.Date(Nobel$birthYear, format = "%Y-%m-%d")
Nobel$birthYear <- format(Nobel$birthYear, format = "%Y")
Nobel$birthYear

Nobel$birthYear <- as.numeric(Nobel$birthYear)

hist(Nobel$birthYear, #x value
     breaks = 200, #number of cells
     xlab = "Birth Year",  #x-axis label
     main = "Histogram of Laureate's birth years", #plot title
     ylim = c(0, 20))
