# Print the following pattern for the given number of rows.
# Note: N is always odd.


# Pattern for N = 5



# The dots represent spaces.

N = int(input())
n1 = (N + 1)//2
i1 = 1 
n2 = N//2
i2 = N//2
while i1 <= n1: 
    spaces = 1
    while spaces <= n1 - i1:
        print(" ", end = "")
        spaces = spaces + 1
    stars = 1
    while stars <= 2*i1 - 1:
        print("*", end = "")
        stars = stars + 1
    print()
    i1 = i1 +1
while i2 >= 1:
    spaces = 1
    while spaces <= n2 - i2 + 1:
        print(" ", end = "")
        spaces = spaces + 1
    stars = 1
    while stars <= 2 * i2 - 1:
        print("*", end = "")
        stars = stars + 1
    print()
    i2 = i2 - 1
