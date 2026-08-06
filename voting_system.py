# Voting System

votes = {
    "Alice": 0,
    "John": 0,
    "Mary": 0
}

while True:

    print("\n===== Voting System =====")
    print("Candidates")

    for candidate in votes:
        print("-", candidate)

    print("Type 'exit' to finish voting.")

    vote = input("Vote: ").title()

    if vote == "Exit":
        break

    if vote in votes:
        votes[vote] += 1
        print("Vote recorded.")
    else:
        print("Invalid candidate.")

print("\n===== Results =====")

for candidate, count in votes.items():
    print(candidate, ":", count)

winner = max(votes, key=votes.get)

print("\nWinner:", winner)