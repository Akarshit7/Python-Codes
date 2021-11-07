# Write a program that performs the tasks of a simple calculator.
# The program should first take an integer as
# input and then based on that integer perform the task as given below.

while True:
    choice = int(input())
    if (choice>=1 and choice<=5):
        num1 = int(input())
        num2 = int(input())
        if choice == 1: 
            res = num1 + num2
            print(res)
        elif choice == 2: 
            res = num1 - num2
            print(res)
        elif choice == 3: 
            res = num1 * num2
            print(res)
        elif choice == 4: 
            res = num1 // num2
            print(res)
        elif choice == 5:
            res = num1 % num2
            print(res)
    elif choice == 6:
        exit()
    else:
        print("Invalid Operation")
