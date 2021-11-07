# Given an integer array A of size n.
# Find and print all the leaders present in the input array. 
# An array element A[i] is called Leader, if all the elements following it (i.e. present at its right) are less than or equal to A[i].
# Print all the leader elements separated by space and in the same order they are present in the input array.

n=int(input())
l=list(map(int,input().split()))
ma=l[-1]
l=l[::-1]
k=[l[0]]
for i in range(1,n):
    if l[i]>=ma:
        ma=l[i]
        k.append(l[i])
k=k[::-1]
print(*k)        
        
