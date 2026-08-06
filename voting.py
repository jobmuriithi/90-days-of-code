#Voting System
Votes = {
    "Sifuna": 0,
    "Ruto": 0,
    "Mudavadi": 0,
    "Gachagua": 0,
}

while True:
    print("\n---- Voting System ----")
    print("Candidates:")

    for candidate in Votes:
        print(candidate)

    print("\nType 'Exit' to end voting.")

    vote = input("Enter your vote: ").title()

    if vote == "Exit":
        break

    if vote in Votes:
        Votes[vote] += 1
        print(f"Thank you for voting for {vote}!")

    else:
        print("Invalid Candidate")


print("\n=========RESULTS==========")

for candidate, count in Votes.items():
    print(candidate,":", count)

winner = max(Votes, key=Votes.get)

print("Winner is : ", winner )



