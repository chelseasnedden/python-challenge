import os

import csv

#current dir
curr_dir = os.getcwd()
#complete file path
filepath = os.path.join(curr_dir,'Resources','election_data.csv')

#init variables
totalcount = 0; khancount = 0; corcount = 0; licount = 0; otcount = 0; fin_votecount = 0

#percent function
def percentage (part, whole):
    return 100 * float(part)/float(whole)

#open/read CSV
with open(filepath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')

     for i in csvreader:
         voterid = i[0]
         country = i[1]
         candidate = i[2]
         #total vote counts
         totalcount = totalcount + 1

         #find vote counts of candidates
         if candidate =="Khan":
            khancount = khancount + 1
         if candidate =="Correy":
            corcount = corcount + 1
         if candidate =="Li":
            licount = licount + 1
         if candidate =="O'Tooley":
            otcount = otcount + 1
            
#define and rename candidates / votes
     candvote = {"Khan": khancount,"Correy": corcount,"Li" :licount, "O'Tooley": otcount}
     #find winner 
     for candidate, value in candvote.items():
         if value > fin_votecount:
            fin_votecount = value
            winner = candidate
# Display results       
print(f'Election Results'+'\n')
print(f'-------------------------------'+'\n')
print(f'Total Votes: {totalcount}'+'\n')
print(f'-------------------------------'+'\n')

print(f'Khan: {percentage(khancount,totalcount):.3f}%  ({khancount})')
print(f'Correy: {percentage(corcount,totalcount):.3f}%  ({corcount})')
print(f'Li: {percentage(licount,totalcount):.3f}%  ({licount})')
print(f'O\'Tooley: {percentage(otcount,totalcount):.3f}%  ({otcount})')
print(f'--------------------------------'+'\n')
print(f'Winner: {winner} '+'\n')
print(f'--------------------------------'+'\n')
