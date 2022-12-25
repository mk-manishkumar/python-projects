
import random

print("Welcome to Rock Paper Scissor Game\n\n\n")

print("Human, it's your turn ! \nChoose among Rock, Paper and Scissor")

choice = ["rock", "paper", "scissor"]

humanWon = 0
cpuWon = 0

while True:
    user = input("Enter the choice: ")
    if user.lower() in ["exit", "quit"]:
        break
    humanChoice = user.lower()
    cpuChoice = random.choice(choice)

    if humanChoice in ["rock", "paper", "scissor"]:
        if (humanChoice == "rock" and cpuChoice == "paper"):
            print("\nCPU won")
            cpuWon = cpuWon + 1
        elif (humanChoice == "rock" and cpuChoice == "scissor"):
            print("\nHuman won")
            humanWon = humanWon + 1
        elif (humanChoice == "paper" and cpuChoice == "scissor"):
            print("\nCPU won")
            cpuWon = cpuWon + 1
        elif (humanChoice == "paper" and cpuChoice == "rock"):
            print("\nHuman won")
            humanWon = humanWon + 1
        elif (humanChoice == "scissor" and cpuChoice == "rock"):
            print("\nCPU won")
            cpuWon = cpuWon + 1
        elif (humanChoice == "scissor" and cpuChoice == "paper"):
            print("\nHuman won")
            humanWon = humanWon + 1
        elif ((humanChoice == "paper" and cpuChoice == "paper") or 
              (humanChoice == "scissor" and cpuChoice == "scissor") or 
              (humanChoice == "rock" and cpuChoice == "rock")):
            print("\nIt's a Draw")
    else:
        print("Invalid Input ! Do it again.\n\n")
        continue

    print("\nDo you wish to continue ? Press Y for Yes and Press N for No\n")
    choose = input("Enter Y/N : ")
    if (choose == 'Y' or choose == 'y'):
        continue
    else:
        break

print("\nGame Over\n")

if(humanWon > cpuWon):
    print(f"Human won by {humanWon} - {cpuWon}")
else:
    print(f"CPU won by {cpuWon} - {humanWon}")
