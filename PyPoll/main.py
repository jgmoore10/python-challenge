import os
import csv

poll_data = os.path.join("Resources", "election_data.csv")

#Variables 
votes = []
candidates = []
results = {}
total_votes=0
win_count=0
win_candidate = ""


#Read CSV File
with open(poll_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csvfile:
        total_votes = total_votes + 1

        candidates_name = row.split(',')[2]       

        if candidates_name not in candidates:
            candidates.append(candidates_name)
            results[candidates_name] = 0
        
        
        results[candidates_name] += 1 


    for row in results:
        votes = results.get(row)
        vote_percent = votes / total_votes



        if (votes > win_count):
            win_count = votes
            win_candidate= row 



print("Election Results")
print("------------------------")
print(f'The total votes cast were: {total_votes}')
print(f'The results for each candidates were:{results}')
print("------------------------")
print(f'The winner was: {win_candidate, win_count}')


#Write text to file
output = open("output.txt",'w')

line1=('Election Results')
line2='------------------------'
line3=str(f'The total votes cast were: {str(total_votes)}')
line4=str(f'The results for each candidate were: {str(results)}')
line5=str(f'------------------------')
line6=str(f'The winner was: {str(win_candidate)} {str(win_count)}')

output.write('{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6))
