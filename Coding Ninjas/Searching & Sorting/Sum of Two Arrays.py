# Two random integer arrays/lists have been given as ARR1 and ARR2 of size N and M respectively. 
# Both the arrays/lists contain numbers from 0 to 9(i.e. single digit integer is present at every index). 
# The idea here is to represent each array/list as an integer in itself of digits N and M.

# You need to find the sum of both the input arrays/list treating them as two integers and put the result in another array/list
# i.e. output array/list will also contain only single digit at every index.

from sys import stdin

def sumOfTwoArrays(arr1, n, arr2, m, output) :
    #Your code goes here
    i=n-1
    j=m-1
    carry =0
    k=max(m,n)
    while i>=0 and j>=0:
        sum=arr1[i]+arr2[j]+carry
        output[k]=sum%10
        carry=sum//10
        i=i-1
        j=j-1
        k=k-1
    while i>=0:
        sum=arr1[i]+carry
        output[k]=sum%10
        i=i-1
        k=k-1
    while j>=0:
        sum=arr2[j]+carry
        output[k]=sum%10
        print(output)
        carry=sum//10
        j=j-1
        k=k-1
    output[0]=carry  
    return output


#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0 :
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
    arr1, n = takeInput()
    arr2, m = takeInput()
    
    outputSize = (1 + max(n, m))
    output = outputSize * [0]
    
    sumOfTwoArrays(arr1, n, arr2, m, output)
    printList(output, outputSize)
    
    t -= 1
