def nested_loop(n):
    for i in range(1, n+1):
        for j in range(i, n+1):
            print(i+j)

nested_loop(2)