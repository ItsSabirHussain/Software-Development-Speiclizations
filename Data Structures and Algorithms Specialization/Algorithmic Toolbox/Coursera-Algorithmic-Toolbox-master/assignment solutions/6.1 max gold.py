import numpy
def mGGGG(parm_WW, parm_nn, pmar_it):
    num_v = numpy.zeros((parm_WW + 1, parm_nn + 1))
    for i in range(1, parm_WW + 1):
        for j in range(1, parm_nn + 1):
            num_v[i][j] = num_v[i][j - 1]
            if pmar_it[j - 1] <= i:
                temp = num_v[i - pmar_it[j - 1]][j - 1] + pmar_it[j - 1]
                if temp > num_v[i][j]:
                    num_v[i][j] = temp
    return (int(num_v[parm_WW][parm_nn]), num_v)
def p_It(value, items, i, j, arr):
    if i == 0 and j == 0:
        arr.reverse()
        return arr
    if value[i][j] == value[i][j - 1]:
        arr.append(0)
        return p_It(value, items, i, j - 1, arr)
    else:
        arr.append(1)
        return p_It(value, items, i - items[j - 1], j - 1, arr)
if __name__ == '__main__':
    num_W, num_n = [int(i) for i in input().split()]
    num_i_w = [int(i) for i in input().split()]
    num_m_w, num_MM = mGGGG(num_W, num_n, num_i_w)
    num_bv = p_It(num_MM, num_i_w, num_W, num_n, [])
    num_o = [str(j) for i, j in enumerate(num_i_w) if num_bv[i]]
    print(f"Weights in knapsack of capacity {num_W}: {' '.join(num_o)}")