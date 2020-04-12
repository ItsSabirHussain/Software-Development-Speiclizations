def merge(lll, rrr):
    num_i, num_j, i_count = 0, 0, 0
    ff = list()
    while num_i < len(lll) and num_j< len(rrr):
        if lll[num_i] <= rrr[num_j]:
            ff.append(lll[num_i])
            num_i += 1
        else:
            ff.append(rrr[num_j])
            i_count += len(lll) - num_i
            num_j += 1

    ff += lll[num_i:]
    ff += rrr[num_j:]
        
    return ff, i_count

def msort(aaa):
    global t_count
    if len(aaa) <= 1:
        return aaa
    mm = len(aaa) // 2

    left_num = msort(aaa[:mm])
    right_num = msort(aaa[mm:])

    s_arr, t = merge(left_num, right_num)
    t_count += t

    return s_arr

t_count = 0
number = int(input())
ss = [int(i) for i in input().split()]
msort(ss)
print(t_count)


