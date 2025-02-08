import random

def guess_number(difficulty):
    difficulty.lower()
    if difficulty=="easy":
        n=11
    if difficulty=="normal":
        n=51
    if difficulty=="hard":
        n=101
    random_number=random.randrange(1,n)
    print(f"The game is set to {difficulty}")
    guess_number=int(input("Enter the number : "))
    attempts=1
    flag=False
    flag_corrrect_answer=False
    while not flag:
        if guess_number==random_number:
            flag=True
        elif guess_number!=random_number:
            print(f"you are wrong {guess_number} is not correct and {attempts} tries till now")
            attempts+=1
            guess_number=int(input())
        if attempts>(n//2) and guess_number!=random_number:
            flag_corrrect_answer=input("enter do you need the flag_corrrect_answer (y,n)")
            flag_corrrect_answer.lower()
            if flag_corrrect_answer=="y":
                flag_corrrect_answer=True
                break
            else:
                flag_corrrect_answer=False
    if flag:
        print(f"you are right {guess_number} is correct and it took you {attempts} attempts to solve")
    if flag_corrrect_answer:
        print(f"the correct answer is {random_number}")

    return "Thanks for playing this game"

def main():
    difficulty=input("Enter the difficulty level (EASY,NORMAL,HARD) : ")
    result=guess_number(difficulty)
    print(result)

main()