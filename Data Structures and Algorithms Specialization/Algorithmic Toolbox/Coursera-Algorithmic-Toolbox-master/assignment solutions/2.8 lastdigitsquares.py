number = int(input())
l_n = number % 60
l_nplus = (number + 1) % 60

def fibonacci(n):
    num_a, num_b = 0, 1
    for _ in range(2, n+1):
        num_c = num_a+num_b
        num_c = num_c% 10
        num_b, num_a = num_c, num_b
    return num_c

if l_n<=1:
    a = l_n
else:
    a = fibonacci(l_n)
if l_nplus<=1:
    b = l_nplus
else:
    b = fibonacci(l_nplus)

print((a*b)%10)