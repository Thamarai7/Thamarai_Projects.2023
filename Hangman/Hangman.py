# word_list = ["advark", "baboon", "camel"]
from hangman_words import word_list
import random

choose = random.choice(word_list)

display = []
word = len(choose)
end_of_game = False
lives = 6
warning = 0
right = 0
from Hangaman_art import logo
print(logo)
print(choose)

for letter in range(word):
    display += "_"
print(display)
while not end_of_game:
    guess = input("Enter your guess ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word):
        letter = choose[position]
        if letter == guess:
            display[position] = letter
            right += 1
            num = word - right
            print(f"Right guess,{num} more guess for complete")
            print(display)
    if guess not in choose:
        lives -= 1
        warning += 1
        print(f"Wrong guess ,warning{warning}")
        if lives == 0:
            end_of_game = True
            print("You lose")
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("Congratulations You achieved hangman")
    from Hangaman_art import stages
    print(stages[lives])