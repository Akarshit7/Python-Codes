# Write a program to do basic string compression. 
# For a character which is consecutively repeated more than once, 
# replace consecutive duplicate occurrences with the count of repetitions.

from sys import stdin

def getCompressedString(string) :
	# Write your code here.
    s = ""
    l = string.split()
    i = 0
    while i < len(string)-1:
        count = 1
        j = i+1
        while j < len(string):
            if l[0][i] == l[0][j]:
                count = count + 1
                i = i + 1
                j = j + 1
                continue
            elif l[0][i]!=l[0][j]:
                break
        if count == 1:
            s = s + l[0][i]
        else:
            s = s + l[0][i] + str(count)
        if j == len(string)-1:
            s = s + l[0][j]
        i = i + 1  
    return s    

# Main.
string = stdin.readline().strip();
ans = getCompressedString(string)
print(ans)
