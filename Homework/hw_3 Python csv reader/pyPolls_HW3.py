import csv
import os
import pandas as pd
candidates = [] 
person = ""
#this will become a 3d array, with the candidate name, total votes, and percentage of votes
votecount = []
percentage = []
everything = []
total = 0
percent = 0.0
winner = 0
n = 0
m = 0

pollResults = open("Resources/pollResults.txt", "w+")

with open('Resources/election_data.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        
        if(row[0] != "Voter ID"): #loop ignores the first line in the excel file
            total += 1
            person = row[2]
            #if candidate is already in list, adds another vote to their tally
            if person in candidates:   
                votecount[candidates.index(person)] += 1
            #if candidate is not in the list, adds them to the list candidates, and sets its corresponding votecountvalue to 1
            else:
                candidates.append(person)
                votecount.append(1)
                   
                
for i in votecount:
    percent = round((i/total)*100.0, 0)
    
    if (percent > winner):
        winner = percent
        n = m
    percentage.append(str(percent) + "%")
    m+= 1
    
everything = list(zip(percentage, votecount))
df = pd.DataFrame( data = everything, columns = ['Percent of Vote', 'Total Number of Votes'], index = candidates)

print("Election pollResults" + "\n----------------------------------------------------")
pollResults.write("\n Election pollResults" + "\n----------------------------------------------------")

print("\n Total Votes: " + str(total) + "\n----------------------------------------------------")
pollResults.write("\n Total Votes: " + str(total) + "\n----------------------------------------------------")

print(df)

for j in range(len(candidates)):
    #print(candidates[j] + ": " + str(percentage[j]) + "% " + "(" + str(votecount[j]) + ")")
    pollResults.write( "\n" + candidates[j] + ": " + str(percentage[j]) + "% " + "(" + str(votecount[j]) + ")")

print("----------------------------------------------------")
pollResults.write("\n ----------------------------------------------------")
        
print("Winner: " + candidates[n])
pollResults.write("Winner: " + candidates[n])
pollResults.close()
        