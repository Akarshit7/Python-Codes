# Given a string S (that can contain multiple words), you need to find the word which has minimum length.
# Note : If multiple words are of same length, then answer will be first minimum length word in the string.
# Words are seperated by single space only.

s=input().split()
l=[]
for i in s:
    l.append(len(i))
print(s[l.index(min(l))])
