# import libraries to use certain functions within Python
import os
import csv

PyPollcsvpath = os.path.join(r"C:\Users\14029\Desktop\BCS Projects\python-challenge\Starter_Code\PyPoll", "Resources", "election_data.csv")

# 
Candidate_List = []

# Set voter counts to 0 
Total_Votes = 0 
CCS_Vote_Count = 0
DG_Vote_Count = 0
RAD_Vote_Count = 0 

# Open the CSV using the UTF-8 encoding 
with open(PyPollcsvpath, encoding = "UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # This will not count the first row in the program
    headers = next(csvreader)

    for row in csvreader:
        
        # Counts the total number of votes cast 
        Total_Votes = Total_Votes + 1
        if row[2] == "Charles Casper Stockham":
            # Total number of votes CCS won
            CCS_Vote_Count += 1
            # Calculate the percentage of votes for CCS
            CCS_vote_percentage = CCS_Vote_Count / Total_Votes * 100

        elif row[2] == "Diana DeGette":
            # Total number of votes for DG
            DG_Vote_Count += 1
            # Calculate percentage of votes for DG
            DG_vote_percentage = DG_Vote_Count / Total_Votes * 100

        elif row[2] == "Raymon Anthony Doane":
            # Total number of votes for RAD
            RAD_Vote_Count += 1
            # Calculate percentage of votes for RAD
            RAD_vote_percentage = RAD_Vote_Count / Total_Votes * 100 
        
        # Find the winner of the election based on popular vote 
        if CCS_Vote_Count > DG_Vote_Count and CCS_Vote_Count > RAD_Vote_Count:
            winner = "Charles Casper Stockham"
        elif DG_Vote_Count > CCS_Vote_Count and DG_Vote_Count > RAD_Vote_Count:
            winner = "Diana DeGette"
        elif RAD_Vote_Count > CCS_Vote_Count and RAD_Vote_Count > DG_Vote_Count:
            winner = "Raymon Anthony Doane"

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(Total_Votes))
print("----------------------------")
print("Charles Casper Stockham: " + str(round(CCS_Vote_Count/Total_Votes*100,3)) + "% " + "(" + str(CCS_Vote_Count) + ")")
print("Diana DeGette: " + str(round(DG_Vote_Count/Total_Votes*100,3)) + "% " + "(" + str(DG_Vote_Count) + ")")
print("Ramon Anthony Doane: " + str(round(RAD_vote_percentage, 3)) + "% " + "(" + str(RAD_Vote_Count) + ")")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")


# Exporting to a text file
PyPoll_output = os.path.join(r"C:\Users\14029\Desktop\BCS Projects\python-challenge\PyPoll" ,"Analysis", "output_file.txt")

with open(PyPoll_output, "w") as file:
    file.write("Election Results\n")
    file.write("----------------------------\n")
    file.write(f"Total Votes: {str(Total_Votes)}\n") 
    file.write("------------------------------\n")
    file.write(f"Charles Casper Stockham: {str(round(CCS_Vote_Count/Total_Votes*100,3))}% ({CCS_Vote_Count})\n")
    file.write(f"Diana DeGette: {str(round(DG_Vote_Count/Total_Votes*100,3))}% ({DG_Vote_Count})\n")
    file.write(f"Ramon Anthony Doane: {str(round(RAD_vote_percentage,3))}% ({RAD_Vote_Count})\n")
    file.write("----------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("----------------------------\n")