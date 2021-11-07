# Write a program to determine if given number is palindrome or not.
# Print true if it is palindrome, false otherwise.

number = int(input())
a = number
reverse = 0
while a > 0:
    digit = a % 10
    reverse = reverse * 10 + digit 
    a = a // 10
if number==reverse:
    print("true")
else:
    print("false")
