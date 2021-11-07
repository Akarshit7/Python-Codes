# Write a program to input an integer N
# and print the sum of all its even
# digits and sum of all its odd digits separately.

N = input()

total = 0
evens = 0

for c in N:
    c = int(c)
    total += c
    if c % 2 == 0:
        evens += c

odds = total - evens

print(evens, odds)
