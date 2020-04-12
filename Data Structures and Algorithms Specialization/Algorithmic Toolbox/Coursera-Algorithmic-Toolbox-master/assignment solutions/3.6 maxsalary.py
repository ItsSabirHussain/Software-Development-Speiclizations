# python3
number = int(input())
l = [int(i) for i in input().split()]


def IGOEqual(dd, m_dd):
    return int(str(dd) + str(m_dd)) >= int(str(m_dd) + str(dd))

def l_number(ll):
    res = []
    
    while ll!=[]:
        max_digit = 0
        for digit in ll:
            if IGOEqual(digit, max_digit):
                max_digit = digit
        res.append(max_digit)
        ll.remove(max_digit)

    return res

print(''.join([str(i) for i in l_number(l)]))
