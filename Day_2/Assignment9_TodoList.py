l = []
flag = 1

while flag == 1:
    choice = int(input("Enter your choice = "))

    if choice == 1:
        task = input("Enter the task to add in list : ")
        l.append(task)
    elif choice == 2:
        remove = int(input("Enter the task to add in list : "))
        l.pop(remove)
    elif choice == 3:
        print(l)

    elif choice==4:
        flag=0
    else:
        print("You entered a wrong choice")