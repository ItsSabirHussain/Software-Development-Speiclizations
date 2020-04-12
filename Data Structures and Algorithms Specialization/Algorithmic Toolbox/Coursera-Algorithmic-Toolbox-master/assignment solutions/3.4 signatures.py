number = int(input())
l = []

for _ in range(number):
    num_a, num_b = [int(i) for i in input().split()]
    l.append((num_a, num_b))

l.sort(key = lambda x: x[1])

ind = 0
coor = []

while ind < number:
    curr = l[ind]
    while ind < number-1 and curr[1]>=l[ind + 1][0]:
        ind += 1
    coor.append(curr[1])
    ind += 1
print(len(coor))
print(' '.join([str(i) for i in coor]))
