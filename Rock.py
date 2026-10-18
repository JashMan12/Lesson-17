import random #importing random module

while True: #iterate loop

    user_action = input("Enter a choice (rock, paper, scissors): ") #take input

    possible_actions = ["rock", "paper", "scissors"]

#using random function

    computer_action = random.choice(possible_actions)

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    if user_action==computer_action:
        print("It is a tie.")
    elif user_action=="rock":
        if computer_action=="scissors":
            print("Human wins.")
        else:
            print("Computer wins.")
    elif user_action=="paper":
        if computer_action=="rock":
            print("Human wins.")
        else:
            print("Computer wins.")
    elif user_action=="scissors":
        if computer_action=="paper":
            print("Human wins.")
        else:
            ("Computer wins.")
    play_again = input("Play again? (y/n): ")

    if play_again != "y":

        break