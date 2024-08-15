def T(n):
    if n ==1:
        return 1
    
    else:
        sum_t = 0
        i = 2
        while n // i > 0:
            sum_t += T(n // i)
            i *= 2
            
        return sum_t + 1

for x in range(1, 21):
    print("when input n is", x, "|", "sum=", T(x))
