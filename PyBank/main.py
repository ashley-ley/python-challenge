# import libraries to use certain functions within Python
import os
import csv

PyBankcsvpath = os.path.join(r"C:\Users\14029\Desktop\BCS Projects\python-challenge\Starter_Code\PyBank" , "Resources" , "budget_data.csv")

# A list to hold all the dates of financial records 
dates = []

# Set variable counts to 0 to begin with
Total_Months = 0
sum_profit = 0
sum_loss = 0 
profit = 0 
totalPL = 0
Greatest_Increase = 0
Greatest_Decrease = 0

# Open the CSV using the UTF-8 encoding 
with open(PyBankcsvpath, encoding = "UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # This will store the header row
    headers = next(csvreader)

    for row in csvreader:
    
        dates.append(row[0])
        
        Total_Months = Total_Months + 1

        profit = int(row[1])
        # If statement to add together the positive and negative values and identify the greatest_inc and greatest_dec
        # totalPL = totalPL + int(row[1])
        if profit > 0:
            sum_profit = sum_profit + profit
            # Finding the Greatest Increase 
            if profit > Greatest_Increase:
                Greatest_Increase = profit
                # Find the index of the highest month
                highest_month_increase = Greatest_Increase
                Greatest_Month = row[0]
        elif profit < 0:
            sum_loss = sum_loss + profit 
            # Find the Greatest Decrease 
            if profit < Greatest_Decrease:
                Greatest_Decrease = profit
                # Find the index of the lowest month
                lowest_month_decrease = Greatest_Decrease
                Lowest_Month = row[0]

# print("sum_profit", sum_profit) & print("sum_loss", sum_loss) will print the sums if need be 
totalPL = sum_profit + sum_loss
        
# total_changePL = sum_profit - sum_loss with rounding 
avg_change = round(totalPL / (Total_Months -1), 1)


# Print the analysis in terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(Total_Months))   
print("Total: " + "$" + str(totalPL))
print("Average Change: " + str((avg_change)))
print("Greatest Increase in Profits: " + Greatest_Month + " $" + str(Greatest_Increase))
print("Greatest Decrease in Profits: " + Lowest_Month + " $" + str(Greatest_Decrease))

# Exporting to a text file
PyBank_output = os.path.join(r"C:\Users\14029\Desktop\BCS Projects\python-challenge\PyBank", "Analysis", "output_file.txt")


with open(PyBank_output, "w") as file: 
    # Change all strings to f strings
    file.write("Financial Analysisn\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {str(Total_Months)}\n") 
    file.write(f"Total: $ {str(totalPL)}\n")
    file.write(f"Average Change: {str(avg_change)}\n")
    file.write(f"Greatest Increase in Profits: {Greatest_Month} (${str(Greatest_Increase)})\n")
    file.write(f"Greatest Decrease in Profits: {Lowest_Month} (${str(Greatest_Decrease)})\n")

print("Analysis report export to " + PyBank_output)

