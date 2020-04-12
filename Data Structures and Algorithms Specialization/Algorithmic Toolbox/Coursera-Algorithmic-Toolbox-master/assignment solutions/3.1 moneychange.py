number = int(input())
c = 0
for i in [10, 5, 1]:
    if number>=i:
        qqqqqqqqqq = number // i
        c += qqqqqqqqqq
        number = number % i
        if number==0:
            print(c)
            quit()

