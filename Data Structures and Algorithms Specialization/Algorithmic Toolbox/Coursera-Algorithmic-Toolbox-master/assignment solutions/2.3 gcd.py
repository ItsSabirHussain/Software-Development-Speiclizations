num_a, num_b = [int(i) for i in input().split()]
def e_gcd(parm_a, parm_b):
    if parm_b == 0:
        print(parm_a)
        quit()
    parm_c = parm_a % parm_b
    e_gcd(parm_b, parm_c)

if num_a>num_b:
    e_gcd(num_a, num_b)
else:
    e_gcd(num_b, num_a)
