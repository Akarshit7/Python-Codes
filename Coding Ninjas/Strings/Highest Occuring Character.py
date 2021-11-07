# For a given a string(str), find and return the highest occurring character.


from sys import stdin


def highestOccuringChar(string) :
	#Your code goes here
    l = list(string)
    chr = 0
    max = 0
    uniq_str=""
    for i in string:
        if i not in uniq_str:
            uniq_str+=i
    for i in uniq_str:
        if max<l.count(i):
            max=l.count(i)
            chr=i
            
    
    return chr
#main
string = stdin.readline().strip();
ans = highestOccuringChar(string)

print(ans)
