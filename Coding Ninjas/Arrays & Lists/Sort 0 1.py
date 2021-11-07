# You have been given an integer array/list(ARR) of size N that contains only integers,
# 0 and 1. Write a function to sort this array/list. 
# Think of a solution which scans the array/list only once and don't require use of an extra array/list.

def sortZeroesAndOne(arr, n):
    nxtzero = 0
    for i in range(n):
        if arr[i] == 0:
            temp = arr[nxtzero]
            arr[nxtzero] = arr[i]
            arr[i] = temp
            nxtzero+= 1

    return arr
t = int(input())
for test in range(t):
    N = int(input())
    arr = [int(x) for x in input().split()]
    arr = sortZeroesAndOne(arr, N)
    for k in arr:
        print(k, end=" ")
    print()
