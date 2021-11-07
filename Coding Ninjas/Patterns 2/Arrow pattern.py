# Print the following pattern for the given number of rows.
# Assume N is always odd.
# Note : There is space after every star.
# Pattern for N = 7
# *
#  * *
#    * * *
#      * * * *
#    * * *
#  * *
# *


n=int(input())
n1=(n//2)+1
i=1
while i<=n1:
    spaces=i-1
    while spaces>=1:
        print(" ",end="")
        spaces-=1
    star=1
    while star<=i:
        print("* ",end="")
        star +=1
    print()
    i=i+1
n2=n//2
i=1
while i<=n2:
    spaces=n2-i
    while spaces>=1:
        print(" ",end="")
        spaces-=1
    star=n2-i+1
    while star>=1:
        print("* ",end="")
        star-=1
    print()
    i=i+1
