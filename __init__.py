from random import randint

easy = 10
hard = 5

def difficult():
    level = input('Enter a game difficulty ').lower()
    if level == 'e':
        return easy
    else:
        return hard


def check_answer(guess, answer, turns):
    if guess > answer:
        print('Too High')
        return turns - 1
    if guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You finded the answer {answer}")


def play_game():

    answer = randint(1, 100)
    guess = 0
    turns = difficult()

    while guess != answer:
        print(f"Remaining {turns} turns you have,Guess it")
        guess = int(input("Enter the number to guess  "))
        turns = check_answer(guess, answer, turns)

        if guess == 0:
            print("you lose")
        else:
            print("Guess Again")


print("Welcome to number guess")
play_game()