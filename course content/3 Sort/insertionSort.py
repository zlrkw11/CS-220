def inssort(a):
    n = len(a)

    for i in range(n):
        j = i

        while j>0 and a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
            j-=1
    return a

a = [5,3,4,1,2]

print(inssort(a))
