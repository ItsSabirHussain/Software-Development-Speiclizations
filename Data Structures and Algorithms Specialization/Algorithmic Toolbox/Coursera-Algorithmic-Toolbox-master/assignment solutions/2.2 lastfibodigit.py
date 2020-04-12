
number = int(input())
if number<=1:
    print(number)
def lastdigitfibo(num):
    num_a, num_b = 0, 1
    for _ in range(num - 1):
        num_c = num_a + num_b
        num_c = num_c%10
        num_b, num_a = num_c, num_b
    print(num_c)

lastdigitfibo(number)