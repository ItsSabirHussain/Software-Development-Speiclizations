number = int(input())
if number == 1:
    print(1)
    print(1)
    quit()
WWW = number
pp = []
for i in range(1, number):
    if WWW>2*i:
        pp.append(i)
        WWW -= i
    else:
        pp.append(WWW)
        break

print(len(pp))
print(' '.join([str(i) for i in pp]))
