# Import OS module
import os

# Import CSV module
import csv

# Path to CSV file
csvpath = os.path.join('Resources', 'budget_data.csv')

total_months = 0
total_net = 0
greatest_inc_amt = ["",9999999999999999999]
greatest_inc_month = ""
greatest_dec_amt = ["", 0]
greatest_dec_month = ""

# Read CSV file in "read" mode. Assign readable file as a new variable
with open(csvpath) as csvfile:

    # Specifies delimiter and variable. Prints this into csv reader 
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read header and skips it
    header = next(csvreader)
    first_row = next(csvreader)

    # Define variables
    total_months += 1
    total_net += int(first_row[1])
    diff_list = []
    month_list = []
    prev_profit = int(first_row[1])

      # Keep track of the current profit, difference in profit, and months 
    for row in csvreader:
        total_months += 1
        curr_profit = row[1]
        total_net += int(row[1])
        diff = (int(row[1])) - (int(prev_profit))
        diff_list += [diff]
        month_list.append(row[0])
        prev_profit = curr_profit
        

        if diff > greatest_inc_amt[1]:
            greatest_inc_amt[0] = row[0]
            greatest_inc_amt[1] = diff
        if diff < greatest_dec_amt[1]:
            greatest_dec_amt[0] = row[0]
            greatest_dec_amt[1] = diff
            
        
# Calculate the average change
avgchange = (sum(diff_list)) / (len(diff_list)) 

# Print output
print("Financial Analysis")
print("--"*15)
print('Total Months:',total_months)
print('Total: $',total_net)
print('Average Change: $',avgchange)
print('Greatest Increase in Profits : ',greatest_inc_month, '($',greatest_inc_amt,')')
print('Greatest Decrease in Profits: ',greatest_dec_month, '($',greatest_dec_amt,')')
