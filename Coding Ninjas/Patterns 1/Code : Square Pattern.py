# Print the following pattern for the given N number of rows.

N=int(input())
i=1
while i<=N:
    j=1
    while j<=N:
        print(N, end ="")
        j+=1
    print()
    i=i+1
