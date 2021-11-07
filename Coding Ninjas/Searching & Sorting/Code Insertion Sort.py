# Provided with a random integer array/list(ARR) of size N, you have been required to sort this array using 'Insertion Sort'.

from sys import stdin

def insertionSort(arr, n) :  
    #Your code goes here
    for i in range(0,n-1):
        for j in range(i+1,0,-1):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
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
    insertionSort(arr, n)
    printList(arr, n)

    t-= 1
