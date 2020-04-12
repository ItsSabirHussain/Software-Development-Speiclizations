import math
def calculate(parm_a, parm_b, parm_op):
    if parm_op == '+':
        return parm_a + parm_b
    elif parm_op == '-':
        return parm_a - parm_b
    else:
        return parm_a * parm_b


def M_A_M(parm_M, parm_m, parm_i, parm_j, parm_op):
    parm_mi = math.inf
    parm_mx = -math.inf
    for k in range(parm_i, parm_j):
        num_a = calculate(parm_M[parm_i][k], parm_M[k + 1][parm_j], parm_op[k])
        num_b = calculate(parm_M[parm_i][k], parm_m[k + 1][parm_j], parm_op[k])
        num_c = calculate(parm_m[parm_i][k], parm_M[k + 1][parm_j], parm_op[k])
        num_d = calculate(parm_m[parm_i][k], parm_m[k + 1][parm_j], parm_op[k])
        parm_mi = min(parm_mi, num_a, num_b, num_c, num_d)
        parm_mx = max(parm_mx, num_a, num_b, num_c, num_d)
    return parm_mi, parm_mx


def g_m_value(parm_od, parm_ops):
    num_n = len(parm_od)
    num_m = [[None for x in range(num_n)] for x in range(num_n)]
    num_M = [[None for x in range(num_n)] for x in range(num_n)]

    for i in range(num_n):
        num_m[i][i] = parm_od[i]
        num_M[i][i] = parm_od[i]

    for s in range(1, num_n):
        for i in range(0, num_n - s):
            j = i + s
            num_m[i][j], num_M[i][j] = M_A_M(num_M, num_m, i, j, parm_ops)

    return num_M[0][num_n - 1]


if __name__ == "__main__":
    num_ex = input()
    num_op, num_ops = [], []
    for i in num_ex:
        if i in ['+', '-', '*']:
            num_op.append(i)
        else:
            num_ops.append(int(i))
    print(g_m_value(num_ops, num_op))
