# Given an array of length N, you need to find and print the sum of all elements of the array.

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
print(sum(arr))
