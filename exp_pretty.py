#Properly formatted output file by Noah Duran
#In this all columns had to be left justified except teh data in the amounts, which had to be right. In addition all had to be 10 spaces in width with an extra two spaces between the first and second columns

with (open('/Users/noahd/Week2/RefFiles/expenses.txt', 'rt',
           encoding='utf-8') as fin):
    #Setting the variable firstrow to true so each time the program goes through the input file it will seperate it out
    firstrow = True
    for line in fin:
        a = line.split(":")
        if firstrow:
            #Printing the Title names left justified with widths of 10 except the descriptions
            print('{:<10s}{:<10s}{:<10s}{:>s}'.format(a[0] + "  ", a[1], a[2], a[3]))
            firstrow = False
        else:
            #Printing the rest of the lines with the amounts category right justified
            print('{:>10s}{:<10s}{:<10s}{:>s}'.format(a[0] + "  ", a[1], a[2], a[3]))
