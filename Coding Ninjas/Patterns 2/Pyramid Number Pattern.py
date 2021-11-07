# Print the following pattern for the given number of rows.
# Pattern for N = 4
#    1
#   212
#  32123
# 4321234

n = int(input())
i = 1
while i <= n:
    spaces = 1
    while spaces <= n - i:
        print(" ", end="")
        spaces = spaces + 1
    j = i
    while j > 0:
        print(j, end="")
        j = j - 1
    k = 2
    while k <= i:
        print(k, end="")
        k = k + 1
    print()
    i = i + 1
