def horilexp(n):
    count = 0
    for i in range(1, n):
        horilexp(i)
        count += 1

    print(count)

horilexp(10)