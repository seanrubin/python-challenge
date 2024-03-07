#Importing Dependencies
import os
import csv
from pathlib import Path

#Declaring File Location
input_file = Path("..", "..", "python-challenge", "PyPoll", "Resources", "election_data.csv")

#Declaring Variables
total_votes = 0
stockham_votes = 0
degette_votes = 0
doane_votes = 0

#Opening CSV in read mode
with open(input_file,newline="", encoding="utf-8") as election:

    #Storing the Contents of the CSV into the Following Variable
    csv_election = csv.reader(election,delimiter=",")

    #Skipping the Header Labels
    header = next(csv_election)

    #Iterate Through the Rows of the CSV
    for row in csv_election:

        #Counting the Voter IDs to a Variable
        total_votes +=1

        #Creating If Statements for the Four Candidates
        if row[2] == "Charles Casper Stockham": 
            stockham_votes +=1
        elif row[2] == "Diana DeGette":
            degette_votes +=1
        elif row[2] == "Raymon Anthony Doane": 
            doane_votes +=1

#Creating Dictionaries for the Candidates and Votes
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [stockham_votes, degette_votes, doane_votes]

#Zipping the Two Lists Together with Candidates Being the Key and Votes Being the Value
candidates_and_votes = dict(zip(candidates,votes))

#Finding the Max Votes to Get the Winner
key = max(candidates_and_votes, key=candidates_and_votes.get)

#Getting the Percents for Each Candidate
stockham_percent = (stockham_votes/total_votes) *100
degette_percent = (degette_votes/total_votes) * 100
doane_percent = (doane_votes/total_votes)* 100

#Printing Out the Results
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {stockham_percent:.3f}% ({stockham_votes})")
print(f"Diana DeGette: {degette_percent:.3f}% ({degette_votes})")
print(f"Raymon Anthony Doane: {doane_percent:.3f}% ({doane_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

#Setting Up the Output File for the Results
output_file = Path("..", "..", "python-challenge", "PyPoll", "Analysis", "Election Results.txt")

with open(output_file, "w") as file:

    #Writing the Results to the Election Results Text Document
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {stockham_percent:.3f}% ({stockham_votes})")
    file.write("\n")
    file.write(f"Diana DeGette: {degette_percent:.3f}% ({degette_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {doane_percent:.3f}% ({doane_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")