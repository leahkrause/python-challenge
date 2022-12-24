# import os module
import os

# import csv module
import csv 

# Path to CSV file
csvpath = os.path.join('/Users/leahkrausetp/Desktop/Leah_UCB/PROJECTS/python-challenge/PyPoll','Resources', 'election_data.csv')

# Define any outside variables
total_votes = 0

# Read CSV file in "read" mode. Assign readable file as a new variable
with open(csvpath) as csvfile:

    # Specifies delimiter and variable. Prints this into csv reader 
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read header and skips it
    header = next(csvreader)
    first_row = next(csvreader)

    # Create lists to store data
    voter_id = []
    candidate = []
    candidates_votes = []

    # Create variables for three places 
    winner = 0
    runner_up = 0
    third_place = 0 

     # Attain individual candidates names without repetition 
    indv_candidates = list(set(candidate))

    # Create a function that provides the total number and percentage each candidate received 
    for row in csvreader:
        
        # Total votes
        voter_id.append((row[0]))
        
        # Candidate list
        candidate.append(row[2])

        # Count up votes per candidate
        if row == indv_candidates[0]:
            winner += 1
        elif row == indv_candidates[1]:
            runner_up += 1
        elif row == indv_candidates[2]:
             third_place += 1 

    # Calculate total number of votes
    total_votes = len(voter_id)

   # Voter percentage per candidate
    winner_percentage = round(winner / total_votes * 100, 3) 
    runner_up_percentage = round(runner_up / total_votes * 100, 3) 
    third_place_percentage = round(third_place / total_votes * 100, 3) 

#################################################################

# Print output
print("Election Results")
print("--"*15)
print("Total Votes: ", total_votes)
print("--"*15)
print()

