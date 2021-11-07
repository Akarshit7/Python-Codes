# Print the following pattern for the given N number of rows.

n=int(input())
currRow=1
while currRow <=n:
    currCol=1
    ch=ord("A") + currRow -1
    while currCol <= currRow:
        print(chr(ch+currCol -1 ),end="")
        currCol+=1
    print()
    currRow+=1
