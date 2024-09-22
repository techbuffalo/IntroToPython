# Author(s): Noah Duran (nduran) and Xun Yang (xunyang) Team 10

#Initializing records2 to be the list that all the original data is sent into
records2 = []

#Function exp_report that overall will strip, format, read, summarize, and output the expense report
def exp_report(filepath):
    try:
        with open(filepath, 'rt', encoding='utf-8') as fin:
            for line in fin:
                columns = line[:-1].split(':')
                records2.append(columns)
        header = records2[0].copy()
        data = records2[1:].copy()

        for d in data:
            d[0] = float(d[0])  # change str to float

        data.sort()

        categories = set()
        for d in data:
            categories.add(d[1])  # column sub-1 contains the categories

        # dictionary of month number to 3-letter month name string

        n2s = {'01': 'Jan',
               '02': 'Feb',
               '03': 'Mar',
               '04': 'Apr',
               '05': 'May',
               '06': 'Jun',
               '07': 'Jul',
               '08': 'Aug',
               '09': 'Sep',
               '10': 'Oct',
               '11': 'Nov',
               '12': 'Dec'}

        for d in data:
            d[2], d[0] = d[0], d[2]

        # Function get cat will be used first to sort list by their category
        def get_cat(category):
            return category[1]

        # Function get date will be used second to sort data2 from lowest to highest date
        def get_date(date):
            return date[0]

        data.sort(key=get_cat)
        data.sort(key=get_date)

        # Moving through data and replacing the numbers rep months with their key value from the dict n2s
        for d in data:
            year = d[0][:4]
            month = d[0][4:6]
            day = d[0][6:8]
            if d[0][4:6] in n2s.keys():
                month = n2s[d[0][4:6]]
            d[0] = day + '-' + month + '-' + year

        # Empty dict to hold the category name and the amount from the expense file
        category_totals = {}
        # Sum of all the expenses
        totalExpenses = 0.0

        # Setting the category totals in the dict to 0 so the key pair is established
        for c in categories:
            category_totals[c] = 0

        for d in data:
            totalExpenses += d[2]
            category = d[1]
            amount = d[2]
            # Checking if the category is listed in the categories set defined earlier, if it is then adding to the total amount
            if category in categories:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

        # Printing out data2 with the calculated totals in the bottom
        print('{2:13s}''{1:<10s}''{0:<10s}''{3:10s}'.format(header[0], header[1], header[2], header[3]))
        for d in data:
            print('{0:13s}''{1:<10s}''{2:>8.2f}  ''{3:10s}'.format(d[0], d[1], d[2], d[3]))
        print(f"Total: {totalExpenses:.2f}".center(48, ' '))
        # print(stringTotalExpenses.center(58, ' '))
        for category, total in category_totals.items():
            print(f"{category.rjust(22, ' ')}: {total:.2f}")
    except FileNotFoundError:
        print('File could not be found.')
        return

#Setting to run the function based on data from expenses.txt if exp_report is run from main
if __name__ == '__main__':
    exp_report('/Users/noahduran/PycharmProjects/Week4/HW4_export/expenses.txt')
