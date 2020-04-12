import math
def distance(num_p1, num_p2):
    return math.sqrt((num_p1[0] - num_p2[0]) ** 2 + (num_p1[1] - num_p2[1]) ** 2)

def c_s_pair(num_p_x, num_p_y, num_delta, num_best_pair):
    l_n_x = len(num_p_x)
    m_x_x = num_p_x[l_n_x // 2][0]
    num_s_y = [x for x in num_p_y if m_x_x - num_delta <= x[0] <= m_x_x + num_delta]
    bbb = num_delta
    l_n_y = len(num_s_y)
    for i in range(l_n_y - 1):
        for j in range(i+1, min(i + 5, l_n_y)):
            num_p, num_q = num_s_y[i], num_s_y[j]
            ddd = distance(num_p, num_q)
            if ddd < bbb:
                num_best_pair = num_p, num_q
                bbb = ddd
    return num_best_pair[0], num_best_pair[1], bbb

def brute_app(ax):
    num_mi = distance(ax[0], ax[1])
    num_p1 = ax[0]
    num_p2 = ax[1]
    l_n_a_x = len(ax)
    if l_n_a_x == 2:
        return num_p1, num_p2, num_mi
    for i in range(l_n_a_x-1):
        for j in range(i + 1, l_n_a_x):
            if i != 0 and j != 1:
                d = distance(ax[i], ax[j])
                if d < num_mi:
                    num_mi = d
                    num_p1, num_p2 = ax[i], ax[j]
    return num_p1, num_p2, num_mi


def c_pair(ax, ay):
    ln_ax = len(ax)
    if ln_ax <= 3:
        return brute_app(ax)
    mid = ln_ax // 2
    Qx = ax[:mid]
    Rx = ax[mid:]
    midpoint = ax[mid][0]
    Qy = list()
    Ry = list()
    for x in ay:
        if x[0] < midpoint:
           Qy.append(x)
        else:
           Ry.append(x)
    (p1, q1, mi1) = c_pair(Qx, Qy)
    (p2, q2, mi2) = c_pair(Rx, Ry)
    if mi1 <= mi2:
        d = mi1
        mn = (p1, q1)
    else:
        d = mi2
        mn = (p2, q2)
    (p3, q3, mi3) = c_s_pair(ax, ay, d, mn)
    if d <= mi3:
        return mn[0], mn[1], d
    else:
        return p3, q3, mi3


def answer(aaa):
    num_ax = sorted(aaa, key=lambda x: x[0])
    num_ay = sorted(aaa, key=lambda x: (x[1], x[0]))
    num_pp, num_ppp, mith = c_pair(num_ax, num_ay)
    return mith


p = list()
n = int(input())
for i in range(n):
    p.append([int(i) for i in input().split()])

print(answer(p))



