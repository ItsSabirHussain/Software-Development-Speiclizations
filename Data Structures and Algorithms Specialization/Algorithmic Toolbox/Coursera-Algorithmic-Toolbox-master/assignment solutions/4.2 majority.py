number = int(input())
ss = [int(i) for i in input().split()]


def d_function(sss, lll, rrr):
    if lll+1==rrr:
        return sss[lll]
    elif lll+2==rrr:
        return sss[lll]
    m = (lll + rrr) // 2
    left_num = d_function(sss, lll, m)
    right_num = d_function(sss, m, rrr)

    num_c1, num_c2 = 0, 0
    for i in sss[lll:rrr]:
        if i == left_num:
            num_c1+=1
        elif i == right_num:
            num_c2+=1
    if num_c1>(rrr - lll)//2 and left_num != -1:
        return left_num
    elif num_c2>(rrr - lll)//2 and right_num != -1:
        return right_num
    else: 
        return -1

print(int(d_function(ss, 0, number) != -1))

