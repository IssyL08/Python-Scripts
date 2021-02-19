import csv
import os

# Files upload
file_to_load = os.path.join("Resources", "election_data.csv")

# Total Vote Counter
total_votes = 0
votes=[]
# Candidate Options and Vote Counters
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row...
    for row in reader:
        votes.append(row[0])
        total_votes += 1

# candidate name per row
        candidate_name = row[2]

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0


        # Vote to candidate count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

#Print results           
print()
print("Election Results")
print("--------------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------------")

print("--------------------------------")   
print(f"Winner:  {winning_candidate}")
print("--------------------------------")

      

  





