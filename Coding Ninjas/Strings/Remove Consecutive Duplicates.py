# For a given string(str), remove all the consecutive duplicate characters.

from sys import stdin

def removeConsecutiveDuplicates(string) :
	# Your code goes here
    str = ""
    l = string.split()
    x = len(l[0])
    for i in range(0,x):
        if i == x-1:
            str = str + l[0][i]
            break
        if l[0][i] == l[0][i+1]:
            continue
        elif l[0][i] != l[0][i+1]:
            str = str + l[0][i]     
    return str 
#main
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)
