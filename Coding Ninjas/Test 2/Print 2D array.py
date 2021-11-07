# Given a 2D integer array with n rows and m columns. Print the 0th row from input n times, 1st row n-1 times…..(n-1)th row will be printed 1 time.
# Input format :

# Line 1 : No of rows(n) & No of columns(m) (separated by space)

# Line 2 : Row 1 elements (separated by space)

# Line 3 : Row 2 elements (separated by space)

# Line 4 : and so on


n,m=map(int,input().split())
for i in range(n):
    a=list(map(int,input().split()))
    for j in range(n-i):
        print(*a)
