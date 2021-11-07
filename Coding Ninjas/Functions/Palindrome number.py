# Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
# Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121

n = int(input())
i = n
x = 0
while (n > 0) :
    y = n % 10
    x = x * 10 + y
    n = n // 10
if ( i == x):
    print("true")
else:
    print("false")
