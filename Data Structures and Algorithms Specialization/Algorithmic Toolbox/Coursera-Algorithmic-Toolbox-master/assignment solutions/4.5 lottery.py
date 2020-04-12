
m_l = list()
num_s, pp = [int(i) for i in input().split()]

for i in range(num_s):
    num_a, num_b = [int(i) for i in input().split()]
    m_l.append((num_a, 'l'))
    m_l.append((num_b, 'r'))

ppp = input().split()
for i in ppp:
    m_l.append((int(i), 'p'))

m_l.sort()

s_count = 0
p_s_map = dict()
for i in m_l:
    if i[1] == 'l': s_count += 1
    elif i[1] == 'r': s_count -= 1
    else:
        p_s_map[i[0]] = s_count

ttt = ''
for i in ppp:
    ttt += str(p_s_map[int(i)]) + ' '
print(ttt[:-1])
    





















