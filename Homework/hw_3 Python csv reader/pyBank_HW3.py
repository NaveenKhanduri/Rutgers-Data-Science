import csv
import os

#print (os.getcwd())

greatMonth = ""
leastMonth = ""
greatest = 0.0
least = 0.0
months = 0
difference = 0.0
total = 0.0
change = []
changeavg = 0.0
prev = 0

results = open("Resources/BankResults.txt", "w+")

with open('Resources/budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if(row[0] != "Date"):   #prevents an error from occuring when the code reads the first row
            months += 1
            difference = int(row[1]) - prev
            total = total + int(row[1])
            change.append(difference)
            if(difference > greatest):
                greatest = difference
                greatMonth = row[0]
            elif(difference < least):
                least = difference
                leastMonth = row[0]
            prev = int(row[1])
for i in change:   #calculate average monthly change"
    changeavg = changeavg + i
average = changeavg/len(change)
    
print("Financial Analysis" + "\n--------------------------------------")
results.write("Financial Analysis" + "\n--------------------------------------")
print("Total Months: " + str(months))
results.write("Total Months: " + str(months))
print("Total Profit: $" + str(total))
results.write("Total Profit: $" + str(total))
print("Greatest increase in profits: " + greatMonth + " ($" +str(greatest) + ")")
results.write("Greatest increase in profits: " + greatMonth + " ($" +str(greatest) + ")")
print("Greatest decrease in profits: " + leastMonth + " ($" + str(least) + ")")
results.write("Greatest decrease in profits: " + leastMonth + " ($" + str(least) + ")")
results.close()
              
            
            