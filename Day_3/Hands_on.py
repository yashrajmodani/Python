# num = int(input("How many students you want to enter: "))
#
# student_list = []
# student_list_avg =[]
# student_tuple = ()
# student_tuple_avg = ()
#
# for i in range(num):
#     name = input("Enter Name: ")
#     age = int(input("Enter Age: "))
#     score1 = int(input("Enter Score 1: "))
#     score2 = int(input("Enter Score 2: "))
#     score3 = int(input("Enter Score 3: "))
#
#     student_tuple = (name,age,score1,score2,score3)
#     # print(student_tuple)
#     student_list.append(student_tuple)
# print(student_list)
#
# for student_tuple in student_list:
#     name, age,score1,score2,score3 = student_tuple
#     student_avg = (score1 + score2 + score3)/3
#
#     student_mark = (name,age,score1,score2,score3,student_avg)
#
#     student_list_avg.append(student_mark)
# print(student_list_avg)
#
# highest_score = 0
# topper = ''
#
# for student_tuple_avg in student_list_avg:
#     name, age,score1,score2,score3,student_avg = student_tuple_avg
#     if highest_score < student_avg:
#         highest_score = student_avg
#         topper = name
#
#     student_tuple_avg = (name,age,score1,score2,score3,student_avg)
#
# print(f'The topper is {topper} ,and score is {highest_score} ')


# _____________________________________________________________________________________
#
#
# t1 = tuple(input("Enter a number: ").split(','))
# t2 = tuple(input("Enter another number: ").split(','))
#
# print(t1)
# print(t2)
#
# t1 = set(t1)
# print(t1)
# t2 = set(t2)
# print(t2)
# print(tuple(t1.intersection(t2)))


# --------------------------------------------------------------------------------

# txt = input("Enter a string: ").split(' ')
# letter = []
# txt = set(txt)
# print(txt)
#
# for word in txt:
#     for i in word:
#         letter.append(i)
#
# print(sorted(set(letter)))
# ----------------------------------------------------------------------------------------