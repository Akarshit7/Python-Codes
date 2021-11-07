# You have been given a sorted(in ascending order) 
# integer array/list(ARR) of size N and an element X.
# Write a function to search this element in the given input array/list
# using 'Binary Search'. Return the index of the element in the
# input array/list. In case the element is not present in the array/list, then return -1.

from sys import stdin


def binarySearch(arr, n, x) :
    #Your code goes here
    min=0
    max=len(arr)-1
    
    while min<=max:
        middle=(min+max)//2
        if x==arr[middle]:
            return middle
        elif x<arr[middle]:
            max=middle-1
        else:
            min=middle+1
    return(-1)

def takeInput() :
    n = int(stdin.readline().strip())
    
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#main
arr, n = takeInput()
t = int(stdin.readline().strip())

while t > 0 :
    
    x = int(input().strip())    
    print(binarySearch(arr, n, x))

    t -= 1
