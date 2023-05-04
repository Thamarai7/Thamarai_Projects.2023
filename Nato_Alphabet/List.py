# #
# # num = []
# #
# # for i in range(1,50):
# #     num.append(i)
# #
# # # square_list = [n*2 for n in num]
# # # print(square_list)
# # # even_list = [n for n in num if n % 3 == 0]
# # # print(even_list)
# #
# # square_list = [n**2 for n in num]
# # print(square_list)
# # with open("file_1.txt") as file_1:
# #     data_1 = file_1.readlines()
# # with open("file_2.txt") as file_2:
# #     data_2 = file_2.readlines()
# # num = [int(num) for num in data_1 if num in data_2]
# # print(num)
# #
#
# # sentence = "Hello i am software developer"
# #
# # dict = {word:len(word) for word in sentence.split()}
# # print(dict)
# import random
# names = ["Alex", "Caroline", "Kevin", "Lewis", "Anderson", "Allen"]
# score_dict = {name: random.randint(1, 100) for name in names}
# print(score_dict)
#
# passed_students = {student: score for (student, score) in score_dict.items() if score > 65}
# print(passed_students)