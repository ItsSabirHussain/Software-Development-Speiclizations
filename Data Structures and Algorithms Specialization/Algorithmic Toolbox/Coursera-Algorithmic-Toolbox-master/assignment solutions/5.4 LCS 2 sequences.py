# python3
import numpy

def L_C_S(parm_s, parm_ss, parm_sss, parm_ssss):
    MMM = numpy.zeros((parm_sss + 1 , parm_ssss + 1))
    for i in range(1, parm_sss + 1):
        for j in range(1, parm_ssss + 1):
            if parm_s[i - 1] == parm_ss[j - 1]:
                MMM[i][j] = MMM[i-1][j-1] + 1
            if parm_s[i - 1] != parm_ss[j - 1]:
                MMM[i][j] = max(MMM[i][j-1], MMM[i-1][j])
    return (int(MMM[parm_sss][parm_ssss]), MMM)
def p_Ss(parm_M, parm_s, parm_ss, parm_i, parm_j, parm_seq):
    if parm_i == 0 or parm_j == 0:
        if parm_seq == []: return None
        return ''.join(parm_seq[::-1])
    if parm_s[parm_i - 1] == parm_ss[parm_j - 1]:
        parm_seq.append(parm_s[parm_i - 1])
        return p_Ss(parm_M, parm_s, parm_ss, parm_i - 1, parm_j - 1, parm_seq)
    if parm_M[parm_i - 1][parm_j] > parm_M[parm_i][parm_j - 1]:
        return p_Ss(parm_M, parm_s, parm_ss, parm_i - 1, parm_j, parm_seq)
    else: 
        return p_Ss(parm_M, parm_s, parm_ss, parm_i, parm_j - 1, parm_seq)
if __name__ == '__main__':
    num_n, num_nn, num_nnn, num_nnnn = int(input()), input(), int(input()), input()
    L_l, MM = L_C_S(num_nn, num_nnnn, num_n, num_nnn)
    ss = p_Ss(MM, num_nn, num_nnnn, num_n, num_nnn, [])
    print(L_l-1)
