"""
Nth term of Fibonacci series F(n), where F(n)
is a function, is calculated using the following formula - """

n= int(input())
def fib(n):
    if n <= 1:
        return n
    i=0
    j=1
    sum_fibbo=1
    count=1
    while count<n:
        sum_fibbo=i+j
        i=j
        j=sum_fibbo
        count+=1

    return  sum_fibbo


if __name__ == '__main__':

    print(fib(n))
