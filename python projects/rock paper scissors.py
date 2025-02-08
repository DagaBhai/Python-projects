import random

print("welcome to the game of rock , paper and scissors")
computer_win=0
user_win=0

options=["rock","paper","scissors"]
round_matches=0
while True:
    user_input=input("you choose (rock/paper/scissors) or q for quit : ").lower()
    if user_input=="q":
        print(f"till the {round_matches} rounds computer won {computer_win} times and you won {user_win} times")
        break
    if user_input not in options:
        continue

    random_pos=random.randrange(0,len(options))
    computer_input=options[random_pos]

    if (user_input=="rock" and computer_input=="paper") or (user_input=="scissors" and computer_input=="rock") or (user_input=="paper" and computer_input=="scissors"):
        print("you win")
        round_matches+=1
        user_win+=1
    elif user_input==computer_input:
        print("Its a tie")
        round_matches+=1
    else:
        print("computer wins")
        round_matches+=1
        computer_win+=1

