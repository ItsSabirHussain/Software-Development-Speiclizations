# Python3
num_m, num_n = [int(i) for i in input().split()]

if num_n<=1:
    print(num_n)
    quit()


l_n = (num_n + 2) % 60
l_m = (num_m + 1) % 60


def fibonacci(n):
    num_a,num_b = 0, 1
    for i in range(2,n+1):
        num_c = num_a+num_b
        num_c = num_c%10
        num_b, num_a = num_c, num_b
    return (num_c-1)
if l_n<=1:
    a = l_n - 1
else:
    a = fibonacci(l_n)
if l_m<=1:
    b = l_m - 1
else:
    b = fibonacci(l_m)
if a>=b:
    print(a-b)
else:
    print(10+a-b)