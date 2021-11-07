# You have been given a random integer array/list(ARR) of size N. You are required to find and return the second largest element present in the array/list.
# If N <= 1 or all the elements are same in the array/list then return -2147483648 or -2 ^ 31(It is the smallest value for the range of Integer)

from sys import stdin


def secondLargestElement(arr, n):
    #Your code goes here
    arr.sort()
    i= n - 2
    x = True
    while i>0:
        if arr[i] == arr[i+1]:
            i = i - 1
            continue
            x = True
        else:
            x = False
            break
    if x:
        return -2147483648
    else:
        return arr[i]
   



#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0



#main
t = int(stdin.readline().rstrip())

while t > 0 : 
    
    arr, n = takeInput()
    print(secondLargestElement(arr, n))

    t -= 1
