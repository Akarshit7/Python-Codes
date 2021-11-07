# Print the following pattern for n number of rows.
# For eg. N = 5

# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    spaces=0
    while spaces<2*n-2*i:
        print(" ",end="")
        spaces=spaces+1
    num=i
    while num>0:
        print(num,end="")
        num-=1
    print()
    i=i+1
