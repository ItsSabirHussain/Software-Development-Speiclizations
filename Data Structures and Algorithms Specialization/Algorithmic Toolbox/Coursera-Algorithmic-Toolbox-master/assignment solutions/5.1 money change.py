import math
m = int(input())
d = [1, 3, 4]
mC = [0] + [math.inf] * m

for i in range(1, m + 1):
    for j in d:
        if i>=j:
            c = mC[i - j] + 1
            if c < mC[i]:
                mC[i] = c

print(mC[m])