# Python3
number, WWW = [int(i) for i in input().split()]
lst = []

if WWW == 0:
    print(0)
    quit()

for _ in range(number):
    num_v, num_w = [int(i) for i in input().split()]
    if num_v == 0:
        continue
    lst.append((num_v, num_w))

lst.sort(key = lambda x: x[0]/x[1], reverse = True)

t_v = 0

for num_v, num_w in lst:
    if WWW==0:
        print(t_v)
        quit()
    aaamt = min(num_w, WWW)
    t_v += aaamt * num_v / num_w
    WWW -= aaamt

print(t_v)

