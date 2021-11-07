# Print the following pattern for the given number of rows.
# Note: N is always odd.


# Pattern for N = 5



# The dots represent spaces.

n = int(input())
n1 = (n+1)//2
n2 = n//2
i = 1
while i <= n1:
    j = 1
    while j <= (n1-i) :
        print(" ",end = "")
        j+=1
    k = 1
    while k<=(2*i)-1:
        print("*",end = "")
        k = k+1
    print()    
    i+=1
    
i = n2
while i>=1:
    j = 1
    while j <= (n2-i+1) :
        print(" ",end = "")
        j+=1
    k = 1    
    while k<=(2*i)-1:
        print("*",end = "")
        k = k+1
    print()
    i=i-1
