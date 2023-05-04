import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter: row.code for (index, row) in data.iterrows()}
def alpha():
    try:
        word = input("Enter a word ").upper()
        nato_list = [dict[letter] for letter in word]
    except KeyError:
        print("Only alphabets are allowed")
        alpha()
    else:
        print(nato_list)

alpha()
