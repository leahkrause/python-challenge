# import os module
import os

# import csv module
import csv 

# Path to CSV file
csvpath = os.path.join('/Users/leahkrausetp/Desktop/Leah_UCB/PROJECTS/python-challenge/PyPoll','Resources', 'election_data.csv')

# Read CSV file in "read" mode. Assign readable file as a new variable
with open(csvpath) as csvfile:

    # Specifies delimiter and variable. Prints this into csv reader 
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read header and skips it
    header = next(csvreader)
    first_row = next(csvreader)