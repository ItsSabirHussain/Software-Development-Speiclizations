import numpy
def E_D(s1, s2):
    num_l_s = len(s1)
    num_l_ss = len(s2)
    M = numpy.zeros((num_l_s+1 , num_l_ss+1))
    for i in range(num_l_ss+1):
        M[0][i] = i
    for i in range(num_l_s+1):
        M[i][0] = i
    for i in range(1, num_l_s+1):
        for j in range(1, num_l_ss+1):
            iii = M[i][j-1]   + 1
            ddd  = M[i-1][j]   + 1
            mmm  = M[i-1][j-1] + 1
            m = M[i-1][j-1]
            if s1[i-1] == s2[j-1]:
                M[i][j] = min(iii, ddd, m)
            if s1[i-1] != s2[j-1]:
                M[i][j] = min(iii, ddd, mmm)
    return (int(M[num_l_s][num_l_ss]), M)

def O_A(MMM, s, ss, ttt, bbb, iii, jjj):
    if iii == 0 and jjj == 0:
        return (' '.join(ttt[::-1]), ' '.join(bbb[::-1]))
    if iii>0 and MMM[iii][jjj] == MMM[iii - 1][jjj] + 1:
        ttt.append(f'|{s[iii - 1]}|')
        bbb.append('|-|')
        return O_A(MMM, s, ss, ttt, bbb, iii - 1, jjj)
    elif jjj>0 and MMM[iii][jjj] == MMM[iii][jjj - 1] + 1:
        bbb.append(f'|{ss[jjj - 1]}|')
        ttt.append('|-|')
        return O_A(MMM, s, ss, ttt, bbb, iii, jjj - 1)
    else:
        ttt.append(f'|{s[iii - 1]}|')
        bbb.append(f'|{ss[jjj - 1]}|')
        return O_A(MMM, s, ss, ttt, bbb, iii - 1, jjj - 1)

if __name__ == '__main__':
    num_s1, num_s2 = input(), input()
    e_dis, M = E_D(num_s1, num_s2)
    t, b = O_A(M, num_s1, num_s2, [], [], len(num_s1), len(num_s2))
    print(e_dis)
