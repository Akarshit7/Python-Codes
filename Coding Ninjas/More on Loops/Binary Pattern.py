# Print the following pattern for the given number of rows.
# Pattern for N = 4
# 1111
# 000
# 11
# 0

n = int(input())
ones = True
while n > 0:
  out = ["1"]*n if ones else ["0"]*n
  ones = not ones
  n -= 1
  print("".join(out))
