# Write a Program to determine if the given number is Armstrong number or not. Print true if number is armstrong, otherwise print false.
# An Armstrong number is a number (with digits n) such that the sum of its digits raised to nth power is equal to the number itself.

def function(n) :
    p = len(str(n))
    sum = 0
    total = n
    for x in range(p):
        sum = sum + ((n%10)**p)
        n = n//10
    return sum
n = int(input())
sum = function(n)
if sum == n :
    print("true")
else :
    print("false")
