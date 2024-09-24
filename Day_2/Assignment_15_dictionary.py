grade_dict = {}
while True:
    student_name = input("Enter your name: ")
    if student_name.lower() == 'done':
        break
    grades = input("Enter your grade: ")
    grade = list(map(int, grades.split(",")))

    grade_dict[student_name] = grade

avg = {}

for student,grade in grade_dict.items():
    avg[student] = sum(grade)/len(grade)

top_student = max(avg, key =avg.get)
print(top_student)

print("\nStudent Average Grades:")
for student, avg in avg.items():
    print(f"{student}: {avg:.2f}")


threshold = int(input("\nEnter the threshold value: "))


print("\nStudents with grades above the threshold:")
for student, grades in grade_dict.items():
    above_threshold = [grade for grade in grades if grade > threshold]
    if above_threshold:
        print(f"{student}: {above_threshold}")
