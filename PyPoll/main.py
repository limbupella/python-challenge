import os
import csv

# Read the election data from the CSV file
csvpath = os.path.join("Resources" , "election_data.csv")

count = 0
candidates = []
winner = []
winner_votes = []
votes_percentage = []

with open(csvpath, newline="") as csvfile:
    election_data = csv.reader(csvfile, delimiter=",")
    csv_header = next(election_data)

    for row in election_data:
        count = count + 1
        candidates.append(row[2])

unique_candidates = list(set(candidates))
winner_votes = []
votes_percentage = []
for candidate in unique_candidates:
    votes = candidates.count(candidate)
    winner_votes.append(votes)
    votes_percentage.append((votes / count) * 100)
max_votes = max(winner_votes)
winner_index = winner_votes.index(max_votes)
winner = unique_candidates[winner_index]

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(count))
print("-------------------------")
for i in range(len(unique_candidates)):
    print(f"{unique_candidates[i]}: {votes_percentage[i]:.3f}% ({winner_votes[i]})")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

output = os.path.join(".","financial_analysis.txt")
with open(output, "w") as new:
    new.write("Election Results\n")
    new.write("-------------------------\n")
    new.write("Total Votes: " + str(count) + "\n")
    new.write("-------------------------\n")
    for i in range(len(unique_candidates)):
        new.write(f"{unique_candidates[i]}: {votes_percentage[i]:.3f}% ({winner_votes[i]})\n")
    new.write("-------------------------\n")
    new.write("Winner: " + winner + "\n")
    new.write("-------------------------\n")