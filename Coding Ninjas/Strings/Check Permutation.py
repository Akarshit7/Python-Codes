# For a given two strings, 'str1' and 'str2', check whether they are a permutation of each other or not

from sys import stdin


def isPermutation(string1, string2) :
    s1=0
    s2=0
    for i in string1:
        s1=s1+ord(i)
    for j in string2:
        s2=s2+ord(j)
    if (s1==s2):
        return True
    return False
#main
string1 = stdin.readline().strip();
string2 = stdin.readline().strip();

ans = isPermutation(string1, string2)

if ans :
    print('true')
else :
    print('false')
