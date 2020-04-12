number = int(input())

if number<=1:
    print(number)
    quit()

def fibonacci(num):
    num_1, num_2 = 0, 1
    for _ in range(num - 1):
        num_3 = num_1 + num_2
        num_2, num_1 = num_3, num_2
    print(num_3)

fibonacci(number)
