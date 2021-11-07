# Print the following pattern for the given N number of rows.
# Pattern for N = 4

# . . .1 . . 1 2 . 1 2 3 1 2 3 4 

# The dots represent spaces.

n=int(input())
i=1
while i<=n:
    spaces=1
    while spaces<=n-i:
        print(' ', end ="")
        spaces=spaces+1
    val=1
    while val <=i:
        print(val,end="")
        val=val+1
    print()
    i=i+1
