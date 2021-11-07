# Print the following pattern for the given N number of rows.

lastNumber = int(input())
for row in range(1, lastNumber+1):
    for column in range (row, 0, -1):
        print(row,end="")
    print("")
