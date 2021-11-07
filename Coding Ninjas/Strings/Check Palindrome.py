# Given a string, determine if it is a palindrome, considering only alphanumeric characters.


from sys import stdin


def isPalindrome(string) :
	# Your code goes here
    s = ""
    count = 0
    for l in string:
        s = s + l
        count = count + 1
    r = ""
    for i in range(count-1,-1,-1):
        r = r + string[i]
    if s == r:
        return True
    else:
        return False
#main
string = stdin.readline().strip();
ans = isPalindrome(string)

if ans :
    print('true')
else :
    print('false')
