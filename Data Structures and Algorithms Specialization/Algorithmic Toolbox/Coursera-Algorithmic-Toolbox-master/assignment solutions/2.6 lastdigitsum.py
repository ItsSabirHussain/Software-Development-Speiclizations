number = int(input())
if number<=1:
    print(number)
    quit()
l = (number + 2) % 60
if l==1:
    print(0)
    quit()
elif l==0:
    print(9)
    quit()
def fibonacci(n):
    num_a,num_b = 0, 1
    for _ in range(2, l + 1):
        num_c = num_a+num_b
        num_c = num_c%10
        num_b, num_a = num_c, num_b
    if num_c!=0:
        print(num_c-1)
    else:
        print(9)
fibonacci(l)
