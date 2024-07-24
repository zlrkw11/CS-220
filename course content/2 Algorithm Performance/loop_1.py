def foo(n):
    i_counter = 0
    j_counter = 0
    for i in range(1, n+1):
        for j in range(1, n**2):
            i_counter+=1
        j_counter+=1
    print("i ", i_counter, "j ", j_counter)
    
foo(3)