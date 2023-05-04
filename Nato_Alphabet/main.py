# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
"""we can convert data frame into dictionary in single line ,but it will create indexes as key and convert 
column value into value pair,so we cant get the exact values we want ,so use dictionary comprehension """
# dict = data.to_dict()
# print(dict)
# print(data[data.letter == "A"])

#
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#
data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter: row.code for (index, row) in data.iterrows()}
word = input("Enter a word ").upper()
nato_list = [dict[letter]for letter in word]
print(nato_list)



