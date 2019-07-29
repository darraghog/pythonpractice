# Rock Paper Scissors Exercise

# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock


# Dictionary: element1 beats elemenet2 
rules = { "rock" : "scissors", "scissors" : "paper", "paper" : "rock" }

def get_input(str):
    valid = False
    while not valid:
        play = input(str + " - enter rock, scissors or paper, or enter to exit: ")
        if play in rules:
            return play

        if play == "":
            exit(0)
        
        print("Invalid entry - try again.\n")

while True:
    player1 = get_input("Player 1")
    player2 = get_input("Player 2")

    if player1 == player2:
        print("\n\tDraw!")
        continue

    if rules[player1] == player2:
        print("\n\tPlayer 1 wins")
    else:
        print("\n\tPlayer 2 wins")
    



    