import numpy
def L_C_S(parm_s, parm_ss, parm_sss, parm_n, parm_nn, parm_nnn):
    M = numpy.zeros((parm_n + 1 , parm_nn + 1, parm_nnn + 1))
    for i in range(1, parm_n + 1):
        for j in range(1, parm_nn + 1):
            for k in range(1, parm_nnn + 1):
                if parm_s[i - 1] == parm_ss[j - 1] == parm_sss[k - 1]:
                    M[i][j][k] = M[i-1][j-1][k-1] + 1
                else:
                    M[i][j][k] = max(M[i-1][j][k], M[i][j-1][k], M[i][j][k-1])
    return (int(M[-1][-1][-1]), M)

def pSs(parm_M, parm_s, parm_ss, parm_sss, parm_i, parm_j, parm_k, parm_seq):
    if parm_i == 0 or parm_j == 0 or parm_k == 0:
        if parm_seq == []: return None
        else : return ''.join(parm_seq[::-1])
    if parm_s[parm_i - 1] == parm_ss[parm_j - 1] == parm_sss[parm_k - 1]:
        parm_seq.append(parm_s[parm_i - 1])
        return pSs(parm_M, parm_s, parm_ss, parm_sss, parm_i - 1, parm_j - 1, parm_k - 1, parm_seq)
    if parm_M[parm_i - 1][parm_j][parm_k] > parm_M[parm_i][parm_j - 1][parm_k]:
        if parm_M[parm_i - 1][parm_j][parm_k] > parm_M[parm_i][parm_j][parm_k - 1]:
            return pSs(parm_M, parm_s, parm_ss, parm_sss, parm_i - 1, parm_j, parm_k, parm_seq)
        else:
            return pSs(parm_M, parm_s, parm_ss, parm_sss, parm_i, parm_j, parm_k - 1, parm_seq)
    else:
        if parm_M[parm_i][parm_j - 1][parm_k]> parm_M[parm_i][parm_j][parm_k - 1]:
            return pSs(parm_M, parm_s, parm_ss, parm_sss, parm_i, parm_j - 1, parm_k, parm_seq)
        else:
            return pSs(parm_M, parm_s, parm_ss, parm_sss, parm_i, parm_j, parm_k - 1, parm_seq)

if __name__ == '__main__':
    num_n, num_s, num_nn, num_ss, num_nnn, num_sss = int(input()), input(), int(input()), input(), int(input()), input()
    L_l, num_M = L_C_S(num_s, num_ss, num_sss, num_n, num_nn, num_nnn)
    print(L_l-1)
    sequence = pSs(num_M, num_s, num_ss, num_sss, num_n, num_nn, num_nnn, [])
