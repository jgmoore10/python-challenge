import os
import csv

poll_data = os.path.join("Resources", "election_data.csv")

#Variables 
votes = []
candidates = []

#Read CSV File
with open(poll_data,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    

#Calculate the total number of votes cast
total_votes = count("Voter ID")

#Calculate a complete list of candidates who received votes


#Calculate the total number of votes each candidate won
Kahn = int(Candidate.count("Kahn"))
Correy = int(Candidate.count("Correy"))
Li = int(Candidate.count("Li"))
O'Tooley = int(Candidate.count("O'Tooley"))

#Calculate the percentage of votes each candidate won
percentage_Kahn = Kahn/total_votes
percentage_Correy = Correy/total_votes
percentage_Li = Li/total_votes
percentage_O'Tooley = O'Tooley/total_votes




#Calculate the winner of the election based on popular vote.