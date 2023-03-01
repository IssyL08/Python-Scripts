import csv
import os

# Files to load and output
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("Analysis", "Election_Analysis_IL.csv")

# Total Votes
total_votes = 0

# Candidates list and counting candidate's votes
candidates = []
candidate_votes = {}

# Winning Candidate and Winning Counts
winning_candidate = ""
winning_count = 0

# Read the csv:create dict.
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row...
    for row in reader:

        # Total votes to count
        total_votes = total_votes + 1

        # count candidates in each row
        candidate_name = row[2]

        # if new candidate in loop:
        if candidate_name not in candidates:

            # add new candidate to list
            candidates.append(candidate_name)

            # count new candidate votes
            candidate_votes[candidate_name] = 0

        # add vote total to new found candidates
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# print results
with open(file_to_output, "w") as csv_file:

    # final vote count
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # elections results to csv
    csv_file.write(election_results)

    # finding winner
    for candidate in candidate_votes:

        # find vote count and percents
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # find winning vote number and winner
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # print candidate name with vote info
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # voter output to csv
        csv_file.write(voter_output)

    # printing into terminal results
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # winning candidate print to csv
    csv_file.write(winning_candidate_summary)
