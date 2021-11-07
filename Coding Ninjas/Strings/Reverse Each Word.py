# Aadil has been provided with a sentence in the form of a string as a function parameter.
# The task is to implement a function so as to print the sentence such that each word in the sentence is reversed.

from sys import stdin


def reverseEachWord(string) :
    
    l = string.split()
    s = ""
    for i in range(0,len(l)):
        for j in range(len(l[i])-1,-1,-1):
            s = s + l[i][j]
        s = s + " "  
    return s    
#main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)
