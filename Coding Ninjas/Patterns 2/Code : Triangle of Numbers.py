# Print the following pattern for the given number of rows.
# Pattern for N = 4



# The dots represent spaces.

n=int(input())
i=1
while i<=n:
    space=n-i
    while space>0:
        print(" ",end="")
        space=space-1
    j=1
    while j<=i:
        print(i+j-1,end="")
        j+=1
    p=i-1
    while p>=1:
        print(i+p-1,end="")
        p=p-1
    print()
    i=i+1
