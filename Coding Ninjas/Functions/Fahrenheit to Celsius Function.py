# Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E)
# and Step Size (W), you need to convert all 
# Fahrenheit values from Start to End at the gap of W,
# into their corresponding Celsius values and print the table.

s=int(input())
e=int(input())
w=int(input())
while True:
    c=0
    if s<=e:
        c=(s-32)*5/9
        print(s,int(c))
        s = s + w

    else:break
