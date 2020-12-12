import os
import csv

poll_data = os.path.join("Resources", "election_data.csv")

#Variables 
votes = []
candidates = []
Kahn_count = int()
Correy_count = int()
Li_count = int()
OTooley_count = int()
results = {}

#Read CSV File
with open(poll_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    next(csvreader)
    

# #Calculate the total number of votes cast
# total_votes = 0

# #Calculate a complete list of candidates who received votes
candidate_list = ["Kahn", "Correy", "Li", "O'Toole"]


# #Calculate the total number of votes each candidate won
# Kahn = int(Candidate.count("Kahn"))
# Correy = int(Candidate.count("Correy"))
# Li = int(Candidate.count("Li"))
# O'Tooley = int(Candidate.count("O'Tooley"))

# #Calculate the percentage of votes each candidate won
# percentage_Kahn = Kahn/total_votes
# percentage_Correy = Correy/total_votes
# percentage_Li = Li/total_votes
# percentage_O'Tooley = O'Tooley/total_votes




# #Calculate the winner of the election based on popular vote.
# #define output path
# output_file = os.path.join("analysis.txt")
print('Election Results')
print('----------------------------------------')
print(f'Total Votes: {count}')
    for canditate in candidates:
        print(f'{candidate}: {percentages[candidate]}% ({votes[candidate]}')
print(f'Winner: {winner')

#Write text to file
with open(textpath,'w') as textfile:
   textfile.write('Election Results\n')
   textfile.write('----------------------------------------')
   textfile.write(f'Total Votes: {count}\n')


   textfile.write(f'Winner: {winner}')