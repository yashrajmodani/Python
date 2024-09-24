# tuples and lists

n = int(input("How many students want to enter"))
min_avg = int(input("enter a threshold avg score:"))

student_list = []
student_list_avg = []
student_tuple = ()
student_tuple_avg = ()

for i in range(n):
    name = input("Student's Name:")
    age = int(input("Student's Age:"))
    score1 = int(input("Student's score:"))
    score2 = int(input("Student's score:"))
    score3 = int(input("Student's score:"))

    student_tuple = (name, age, score1, score2, score3)
    print(student_tuple)
    student_list.append(student_tuple)

for student_tuple in student_list:
    name, age, score1, score2, score3 = student_tuple
    student_avg = (score1 + score2 + score3) / 3

    student_marks = (name, age, score1, score2, score3, student_avg)

    student_list_avg.append(student_marks)

    print(student_list_avg)

highest_score = 0
topper = ""

for student_tuple_avg in student_list_avg:
    name, age, score1, score2, score3, student_avg = student_tuple_avg
    if highest_score < student_avg:
        highest_score = student_avg
        topper = name

    student_tuple_avg = (name, age, score1, score2, score3, student_avg)
print(f"The topper is {topper}, and score is {highest_score}")
