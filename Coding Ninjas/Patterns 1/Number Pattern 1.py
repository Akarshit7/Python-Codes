# Print the following pattern for the given N number of rows.

# 1
# 11
# 111
# 1111

n=int(input())
for i in range (0,n):
    for j in range (0,i+1):
        print(1,end="")
    print("")
