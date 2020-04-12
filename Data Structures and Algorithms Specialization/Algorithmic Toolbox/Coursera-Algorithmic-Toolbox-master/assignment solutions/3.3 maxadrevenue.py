number = int(input())
num_a = [int(i) for i in input().split()]
num_b = [int(i) for i in input().split()]
num_a.sort()
num_b.sort()
res = sum([num_a[i] * num_b[i] for i in range(number)])
print(res)