
num_a, num_b = [int(i) for i in input().split()]

def e_gcd(parm_a, parm_b):
    if parm_b == 0:
        return parm_a
    num_c = parm_a % parm_b
    return e_gcd(parm_b, num_c)

if num_a>num_b:
    gcd = e_gcd(num_a, num_b)
else:
    gcd = e_gcd(num_b, num_a)

print(num_a * num_b // gcd)