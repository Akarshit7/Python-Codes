# You have been given a random integer array/list(ARR) of size N. Write a function that rotates the given array/list by D elements(towards the left).

from sys import stdin


def rotate(arr, n, d):
    #Your code goes here
    x = []
    i= d
    for i in range(d,n):
        x.append(arr[i])
        
    i = 0
    for i in range(0,d):
        x.append(arr[i])
    
    a = 0
    for a in range(n):
        arr[a]=x[a]
        

#Taking Input Using Fats I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0



#Taking Input Using Fats I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list 
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    rotate(arr, n, d)
    printList(arr, n)
    
    t -= 1
