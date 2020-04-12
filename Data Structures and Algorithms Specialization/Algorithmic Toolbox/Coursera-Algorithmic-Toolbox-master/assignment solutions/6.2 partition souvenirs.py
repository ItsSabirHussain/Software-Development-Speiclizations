import numpy
def part(parm_W, parm_n, parm_i):
    num_c = 0
    n_v = numpy.zeros((parm_W + 1, parm_n + 1))
    for i in range(1, parm_W + 1):
        for j in range(1, parm_n + 1):
            n_v[i][j] = n_v[i][j-1]
            if parm_i[j - 1]<=i:
                temp = n_v[i - parm_i[j - 1]][j - 1] + parm_i[j - 1]
                if temp > n_v[i][j]:
                    n_v[i][j] = temp
            if n_v[i][j] == parm_W: num_c += 1
    if num_c < 3: print('0')
    else: print('1')
if __name__ == '__main__':
    number = int(input())
    num_i_w = [int(i) for i in input().split()]
    num_t_w = sum(num_i_w)
    if number<3:
        print('0')
    elif num_t_w%3 != 0:
        print('0')
    else:
        part(num_t_w // 3, number, num_i_w)
        