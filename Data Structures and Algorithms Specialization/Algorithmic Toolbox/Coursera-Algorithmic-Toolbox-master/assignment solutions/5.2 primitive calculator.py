import math
n = int(input())
n_o = [0, 0] + [math.inf] * (n - 1)

for i in range(2, n+1):
    t1, t2, t3 = [math.inf] * 3

    t1 = n_o[i - 1] + 1
    if i%2 == 0: t2 = n_o[i // 2] + 1
    if i%3 == 0: t3 = n_o[i // 3] + 1
    m_ops = min(t1, t2, t3)
    n_o[i] = m_ops

print(n_o[n])

numbers = [n]
while n!=1:
    if n%3 ==0 and n_o[n]-1 == n_o[n // 3]:
        numbers += [n // 3]
        n = n//3
    elif n%2 ==0 and n_o[n]-1 == n_o[n // 2]:
        numbers += [n // 2]
        n = n//2
    else:
        numbers += [n - 1]
        n = n - 1

print(' '.join([str(i) for i in numbers][::-1]))