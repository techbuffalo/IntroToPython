#Totals of expenses file by Noah Duran
with (open('/Users/noahd/Week2/RefFiles/expenses.txt', 'rt',
           encoding='utf-8') as fin):
    #Starting by setting all the final totals to zero
    totalExpenses = 0
    febExpenses = 0
    marExpenses = 0
    travelExpenses = 0
    mealExpenses = 0
    supplyExpenses = 0
    utilExpenses = 0

    #Creating a variable called firstrow so that the titles of categories can be separated from the numbers in the file
    firstrow = True
    for line in fin:
        a = line.split(":")
        if firstrow:
            firstrow = False
        else:
            #Expenses puts all the inputs from the first column into one list and converts them into a float
            expenses = float(a[0])
            #Category puts all the inputs from the second column into one list
            category = a[1]
            #Dates puts all the inputs from the third column into one list then converts them into int
            dates = int(a[2])


            totalExpenses += expenses

            #Since the date format is YYYYMMDD this number is the maximum before 02 turns into 03
            if dates <= 20170299:
                febExpenses += expenses
            else:
                marExpenses += expenses

            #Series of if statements to get the amounts from the corresponding category types
            if category == 'travel':
                travelExpenses += expenses
            if category == 'meal':
                mealExpenses += expenses
            if category == 'supply':
                supplyExpenses += expenses
            if category == 'util':
                utilExpenses += expenses

print("Total of all expenses: ", totalExpenses)
print("Total of Feb expenses: ", '{:.2f}'.format(febExpenses)) #Formatting the expenses to have two decimal points
print("Total of Mar expenses: ", '{:.2f}'.format(marExpenses)) #Formatting the expenses to have two decimal points
print("Total travel expenses: ", travelExpenses)
print("Total meal expenses: ", mealExpenses)
print("Total supply expenses: ", supplyExpenses)
print("Total util expenses: ", utilExpenses)

