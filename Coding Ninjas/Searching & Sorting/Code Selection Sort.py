# Provided with a random integer array/list(ARR) of size N, you have been required to sort this array using 'Selection Sort'.

from sys import stdin

def selectionSort(arr, n) :
    #Your code goes here
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
                continue
            if arr[i]<=arr[j]:
                continue
    return arr  
#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    selectionSort(arr, n)
    printList(arr, n)

    t-= 1
