#HW3.1 File created by Noah Duran 

#Inititalizing all the lists that will be used
records = []
records2 = []

with (open('/Users/noahduran/PycharmProjects/Week3/expenses.txt', 'rt',
           encoding='utf-8') as fin):
    #With the file open the first time, strip out all line separators and append the list records
    for line in fin:
        x = line.strip('\n')
        records.append(x)

#Print each line in records out and show no double-spacing
print("Section 1a\n")
for line in records:
    print(line)

#Opening the file the second time
with (open('/Users/noahduran/PycharmProjects/Week3/expenses.txt', 'rt',
           encoding='utf-8') as fin):
    #With the file open again strip the newline and separate by the colon
    for line in fin:
        column = line.strip('\n').split(':')
        records2.append(column)

#Printing records2, which is the list of list
print("\nSection 1b\n")
for line in records2:
    print(line)

#Making copy of records2 then sorting
r2_copy = records2.copy()
r2_copy.sort()
print("\nSection 1c\n")
for row in r2_copy:
    print(row)
#By sorting r2_copy the output is not sorted by dollar amount it's sorted by ASCII value of the first character

#Creating a list for the headers and then one for the data in the file
header = records2[0].copy()
data = records2[1:].copy()

print("\nSection 1d\n")
print(header)
for d in data:
     print(d)

#Looping through the list in data, changing the first value to a float, then removing data that was in place and putting in the float
firstrow = True
for line in data:
    if firstrow:
        numberAmount = float(line[0])
        #Used pop to remove the first item in the list, then used insert to replace it with number amount
        line.pop(0)
        line.insert(0, numberAmount)
    else:
        firstrow = False

print("\nSection 1e\n")
print(header)
for d in data:
     print(d)

#Sorting the data so that it will be in order by dollar amount.
data.sort()
print("\nSection 1f\n")
print(header)
for d in data:
     print(d)

#Creating a set for the various categories
categories = set()

firstrow = True
secondrow = True
for line in data:
    if firstrow:
        firstrow = False
    elif secondrow:
        #Every second value in the line from the list data will be added to categories if it's new
        categories.add(line[1])
    else:
        secondrow = False

print("\nSection 1g")
print("There are", len(categories), "expense categories.")
for c in categories:
    print(c)
print('\n')

#Creating dictionary n2s to find the month of the file
n2s = {
    '01':'Jan'
    ,'02':'Feb'
    ,'03':'Mar'
    ,'04':'Apr'
    ,'05':'May'
    ,'06':'Jun'
    ,'07':'Jul'
    ,'08':'Aug'
    ,'09':'Sep'
    ,'10':'Oct'
    ,'11':'Nov'
    ,'12':'Dec'
}
#Looping through n2s to make a table
print("\nSection 1h\n")
print('{:<5s}'.format('Key'), '{:<5s}'.format('Value'))
for x in n2s.keys():
    print('{:<5s}'.format(x), '{:<5s}'.format(n2s[x]))
