# Print the following pattern
# Pattern for N = 4



# The dots represent spaces.

n=int(input())
i=0
while i<n:
    space=n-i-1
    while space>0:
        print(" ",end="")
        space=space-1
    star=i+1
    while star>0:
        print("*",end="")
        star=star-1
    star=i
    while star>=1:
        print("*",end="")
        star=star-1
    print()
    i=i+1
