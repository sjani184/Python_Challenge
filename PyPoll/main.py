import os
import csv

input_path = os.path.join('.' , 'PyPoll', 'Resources', 'election_data.csv')

total_votes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0


with open(input_path, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    row = next(csvreader)

    total_votes += 1

    for row in csvreader:

        total_votes += 1

        if str(row[2]) == "Khan":
            Khan_votes += 1
        elif str(row[2]) == "Li": 
            Li_votes += 1
        elif str(row[2]) == "Correy": 
            Correy_votes += 1
        else:
            OTooley_votes += 1
            
Khan_percentage = Khan_votes/total_votes
Li_percentage = Li_votes/total_votes
Correy_percentage = Correy_votes/total_votes
OTooley_percentage = OTooley_votes/total_votes

winner = max(Khan_votes, Li_votes, Correy_votes, OTooley_votes)

if winner == Khan_votes:
    winner_name = "Khan wins!"
elif winner == Li_votes:
    winner_name ="Li wins!"
elif winner == Correy_votes:
    winner_name ="Correy wins!"
else:
    winner_name ="O'Tooley wins!"


output_path = os.path.join('.', 'PyPoll', 'Analysis', 'PyPoll_Analysis.text')

with open(output_path, 'w',) as txtfile:

    txtfile.write("Election Results")
    txtfile.write('\n' + "----------------------------")
    txtfile.write('\n' + "Total Votes: " + str(total_votes))
    txtfile.write('\n' + "----------------------------")
    txtfile.write('\n' + "Khan: " + "{:.2%}".format(Khan_percentage) + " (" + str(Khan_votes) + ")")
    txtfile.write('\n' + "Correy: " + "{:.2%}".format(Correy_percentage) + " (" + str(Correy_votes) + ")")    
    txtfile.write('\n' + "Li: " + "{:.2%}".format(Li_percentage) + " (" + str(Li_votes) + ")")    
    txtfile.write('\n' + "O'Tooley: " + "{:.2%}".format(OTooley_percentage) + " (" + str(OTooley_votes) + ")")         
    txtfile.write('\n' + winner_name)

print("Election Results")
print('\n' + "----------------------------")
print('\n' + "Total Votes: " + str(total_votes))
print('\n' + "----------------------------")
print('\n' + "Khan: " + "{:.2%}".format(Khan_percentage) + " (" + str(Khan_votes) + ")")
print('\n' + "Correy: " + "{:.2%}".format(Correy_percentage) + " (" + str(Correy_votes) + ")")    
print('\n' + "Li: " + "{:.2%}".format(Li_percentage) + " (" + str(Li_votes) + ")")    
print('\n' + "O'Tooley: " + "{:.2%}".format(OTooley_percentage) + " (" + str(OTooley_votes) + ")")         
print('\n' + winner_name)