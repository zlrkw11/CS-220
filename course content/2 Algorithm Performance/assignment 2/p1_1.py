def roticeol(n):
    counter = 0
    for i in range(1, 2*n+1):
        for j in range(i, 3*n+1):
            counter+=1
    print(counter)

roticeol(4)