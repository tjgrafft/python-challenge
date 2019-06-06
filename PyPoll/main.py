import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

# Lists to store data
candidate = []
votes = {}

# with open(budget_data, newline="", encoding='utf-8') as csvfile:
with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
        # Add candidate
        candidate.append(row[2])

    for x in candidate:
        if x not in votes:
            votes[x] = 1
        else:
            votes[x] += 1

    


#Total Votes
total_votes = len(candidate)


FO=("Election Results\n")
FO+=("------------------------\n")
FO+=("Total Votes: " + str(total_votes)+"\n")
FO+=("------------------------\n")

#Each Candidates Votes 

for x, y in votes.items():
    percent = round((float(y)/total_votes) * 100 , 2)
    FO+=(x + ": " + str(percent) + "00%"+ " (" + str(y) + ")\n")  
    
    
#Winner
win_vote = ""
kvote = 0
for x, y in votes.items():
	if y > kvote :
		kvote = y
		win_vote = x


#Print final Output
FO+=("------------------------\n")
FO+=("Winner: " + str(win_vote)+"\n")
FO+=("------------------------\n")
print(FO)

#############################################################


file1 = open("results.txt","w") 

file1.write(FO)


file1.close()


