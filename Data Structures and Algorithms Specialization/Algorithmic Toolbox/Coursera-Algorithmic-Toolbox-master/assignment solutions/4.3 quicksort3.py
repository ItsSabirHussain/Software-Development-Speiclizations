# python3
import random
import time
def q_sort(aaa, lll, rrr):
    if lll + 1 >= rrr:
        return
    mmm = random.randint(lll, rrr - 1)
    aaa[lll], aaa[mmm] = aaa[mmm], aaa[lll]
    num_m1, num_m2 = part(aaa, lll, rrr)
    q_sort(aaa, lll, num_m1)
    q_sort(aaa, num_m2 + 1, rrr)
def part(arr, l, r):
    num_m2 = l
    for i in range(l+1, r):
        if arr[i] <= arr[l]:
            arr[num_m2+1], arr[i] = arr[i], arr[num_m2+1]
            num_m2 += 1
    arr[l], arr[num_m2] = arr[num_m2], arr[l]
    num_m1 = l
    for i in range(l, num_m2):
        if arr[i] < arr[num_m2]:
            arr[i], arr[num_m1] = arr[num_m1], arr[i]
            num_m1 += 1
    return num_m1, num_m2

def c_a(size):
    return [random.choice(list(range(10))) for _ in range(size)]

sss = c_a(100000)
q_sort(sss, 0, 100000)
print(sss)
t2 = time.time()

    

