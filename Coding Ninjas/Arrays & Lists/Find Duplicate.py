# You have been given an integer array/list(ARR)
# of size N which contains numbers from 0 to (N - 2).
# Each number is present at least once. That is, if N = 5,
# the array/list constitutes values ranging from
# 0 to 3 and among these, there is a single integer 
# value that is present twice. You need to find
# and return that duplicate number present in the array.


import sys

def unique(arr,n):
    for i in range(n):
        for j in range(n):
            if i!=j:
                if arr[i]==arr[j]:
                    return arr[i]
                else:
                    pass
                
t=int(input())
for test in range(t):
    N=int(input())
    arr1=[int(x) for x in input().split()]
    result= unique(arr1,N)
    print(result)
