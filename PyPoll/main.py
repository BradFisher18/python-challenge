import os
import csv
from collections import Counter

#Create path to csv file
election_data_csv = os.path.join("Resources", "election_data.csv")

#Read csv file
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Store header row
    header = next(csv_reader)
  
    #Define variables
    number_of_votes = 0 
    candidate = []
    candidate_name = []
    candidate_votes = {}
    winner_votes = 0
        
    #Loop through the rows in csv file
    for row in csv_reader:
        
        #Count number of votes
        number_of_votes +=1
        
        #Store candidate selection in list
        candidate.append(row[2])

        #add vote count of each candidate to dictionary
        if row[2] in candidate_name:
            candidate_votes[row[2]] += 1

        else:
            candidate_name.append(row[2])
            candidate_votes[row[2]] = 1

    #Print outputs
    print(f"Election Results")
    print(f"---------------------------")
    print(f"Total Votes: {number_of_votes}")
    print(f"---------------------------")

    #find vote percentage for each candidate and print it
    for name, votes in candidate_votes.items():
        print(f"{name}: {round((votes / number_of_votes)*100, 3)}% ({votes} votes)")
        
        #find the winning candidate
        if votes > winner_votes:
            winner_votes = votes
            winning_candidate = name
    
    #print remaining rows
    print(f"---------------------------")
    print(f"Winner: {winning_candidate}") 
    print(f"---------------------------")

#Output to new CSV file
output_path = os.path.join("analysis", "poll_results.csv")

with open(output_path, 'w') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow([f"Election Results"])
    csvwriter.writerow([f"---------------------------"])
    csvwriter.writerow([f"Total Votes: {number_of_votes}"])
    csvwriter.writerow([f"---------------------------"])

    for name, votes in candidate_votes.items():
        csvwriter.writerow([f"{name}: {round((votes / number_of_votes)*100, 3)}% ({votes} votes)"])

    csvwriter.writerow([f"---------------------------"])
    csvwriter.writerow([f"Winner: {winning_candidate}"])
    csvwriter.writerow([f"---------------------------"])