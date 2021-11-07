# Given a number N, figure out if it is a 
# member of fibonacci series or not. 
# Return true if the number is member of fibonacci series else false.

# Fibonacci Series is defined by the recurrence
#     F(n) = F(n-1) + F(n-2)
# where F(0) = 0 and F(1) = 1

n=int(input())
c=0
a=1
b=1
if n==0 or n==1:
    print("Yes")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print("true")
    else:
        print("false")
