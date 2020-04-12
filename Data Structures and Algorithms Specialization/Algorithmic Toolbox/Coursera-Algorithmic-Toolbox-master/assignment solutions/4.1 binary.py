ss = [int(i) for i in input().split()]
ss_seq = [int(i) for i in input().split()]
number = ss[0]
ss = ss[1:]

def b_search(sss, eee, rrr):
    l = 0
    while l<=rrr:
        m = (l + rrr) // 2
        if eee > sss[m]:
            l = m + 1
        elif eee < sss[m]:
            rrr = m - 1
        else:
            return m
    return -1

sln = list()
for i in ss_seq[1:]:
    ans = b_search(ss, i, number - 1)
    sln.append(ans)
print(' '.join([str(i) for i in sln]))

