#This was all the code from the 8 various tasks in the Instructions files also in this branch

#Initial list of Fahrenheit temps to convert to C
fahrenheitTempsStart = [0, 32, 45, 60, 70, 95, 212] #set the original list to an array
convertedCelStart = [] #Empty array to put the converted temps into

#This for loop will iterate through the orig list array and then append the empty array
for f in fahrenheitTempsStart:
    celConvert = 5/9 * (f - 32)
    convertedCelStart.append(celConvert)

print(convertedCelStart)

#Initial list of Celsius temps to convert to F, with the same concept as F > C
celsiusTempsStart = [0, 10, 15, 20, 25, 30, 100]
convertedFahrStart = []

#This or loop will iterate through the Celsius array and append the empty
for c in celsiusTempsStart:
    fahrConvert = (c * (9/5)) + 32
    convertedFahrStart.append(fahrConvert)

print(convertedFahrStart)


#Sample table to work off of

"""
Date    Hi(F)  Lo(F)  %Hum
AUG 30     79     64    60
AUG 31     82     66    20
SEP  1     85     68    20
SEP  2     85     68    30
SEP  3     87     69    30
SEP  4     87     69    20
SEP  5     87     69    20
SEP  6     85     67    20
SEP  7     81     63    30
SEP  8     79     61    20
SEP  9     77     61    20
SEP 10     77     59    20
SEP 11     77     59    20
SEP 12     77     59    20
SEP 13     77     59    50
"""

#Array for the dates, added space to dates that are single digit for better view when printed
dt = ["AUG 30", "AUG 31", "SEP 1 ", "SEP 2 ", "SEP 3 ", "SEP 4 ", "SEP 5 ", "SEP 6 ", "SEP 7 ", "SEP 8 ", "SEP 9 ", "SEP 10", "SEP 11", "SEP 12", "SEP 13"]

#Array for the Hi temps
hi = [79, 82, 85, 85, 87, 87, 87, 85, 81, 79, 77, 77, 77, 77, 77]

#Array for the Lo Temps
lo = [64, 66, 68, 68, 69, 69, 69, 67, 63 ,61, 61, 59, 59, 59, 59]

#Array for the Humidity
hm = [60, 20, 20, 30, 30, 20, 20, 20, 30 , 20, 20, 20, 20, 20, 50]


#Original attempt at getting the table to formulate being flush left. It required me adding a space to the single digit dates as noted above
print("Date ", "   Hi(F) ", "Lo(F) ", "%Hum")
num_days = len(dt)
for i in range(num_days):
    print(dt[i], '{: >4}'.format(hi[i]), '{: >6}'.format(lo[i]), '{: >6}'.format(hm[i]))

#Copies of each of the arrays
hi_copy = hi
lo_copy = lo
hm_copy = hm

#Calculations to find the mean of each array
hi_mean = sum(hi) / len(hi)
lo_mean = sum(lo) / len(lo)
hm_mean = sum(hm) / len(hm)

#Sorting arrays then finding the median & std deviation of each array using the library of statistics
import statistics

hi_ascending = sorted(hi_copy)
lo_ascending = sorted(lo_copy)
hm_ascending = sorted(hm_copy)

hi_median = statistics.median(hi_ascending)

lo_median = statistics.median(lo_ascending)

hm_median = statistics.median(hm_ascending)

hi_std_dev = statistics.stdev(hi_ascending)

lo_std_dev = statistics.stdev(lo_ascending)

hm_std_dev = statistics.stdev(hm_ascending)

#Print statements to output the mean, median, and sample standard deviant
print("The mean of the tables are ", "\n", "Hi: ", hi_mean, "\n", "Lo: ", lo_mean, "\n", "Hm: ", hm_mean, "\n")
print( "The median of the tables are ", "\n", "Hi: ", hi_median, "\n", "Lo: ", lo_median, "\n", "Hm: ", hm_median, "\n")
print( "The standard deviation of the tables are ", "\n", "Hi: ", hi_std_dev, "\n", "Lo: ", lo_std_dev, "\n", "Hm: ", hm_std_dev, "\n")

#Using the method explained in part(g) formatting the table right based
dt2 = ["AUG 30", "AUG 31", "SEP 1", "SEP 2", "SEP 3", "SEP 4", "SEP 5", "SEP 6", "SEP 7", "SEP 8", "SEP 9", "SEP 10", "SEP 11", "SEP 12", "SEP 13"]
hi2 = [107, 109, 104, 101, 99, 98, 95, 98, 98, 102, 104, 101, 99, 96, 99]
lo2 = [78, 80, 79, 78, 77, 78, 78, 78, 77, 80, 81, 80, 78, 77, 78]
hm2 = [15, 8, 12, 13, 9, 8, 8, 10, 10, 10, 12, 8, 15, 15, 12]

print('{:<6s}{:>7s}{:>7s}{:>6s}'.format('Date', 'Hi(F)', 'Lo(F)', '%Hum'))
num_days = len(dt2)
for i in range(num_days):
    print('{:<6s}{:>7d}{:>7d}{:>6d}'.format(
dt2[i], hi2[i], lo2[i], hm2[i]), "\n")
    
#Created empty arrays to append the converted temperatures into
hi2_cel_conversion = []
lo2_cel_conversion = []
#Using the same method as before, converting the temps into Cel then appending the empty arrays
for i in hi2:
    celConvert = 5/9 * (i - 32)
    hi2_cel_conversion.append(celConvert)
    
for i in lo2:
    celConvert = 5/9 * (i - 32)
    lo2_cel_conversion.append(celConvert)

#Use similar method as above, changing the 7s for hi and lo temps to 7.2f to accommodate decimal points
print('{:<6s}{:>7s}{:>7s}{:>6s}'.format(
          'Date', 'Hi(F)', 'Lo(F)', '%Hum'))
num_days = len(dt2)
for i in range(num_days):
    print('{:<6s}{:>7.2f}{:>7.2f}{:>6d}'.format(
dt2[i], hi2_cel_conversion[i], lo2_cel_conversion[i], hm2[i]), "\n")
    

#Creating the table of integers 1-19 with 6 decimal points
#Collumns will be cubed root, square root, the integer, squared, and cubed 
for i in range(0,20):
    print("{:12.6f} {:12.6f} {:12d} {:12d} {:12d}".format(i**(1/3), i**(1/2), i, i*i, i*i*i))
