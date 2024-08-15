def inssort(a):
    counter = 0
    n = len(a)

    for i in range(n):
        j = i

        while j>0 and a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
            counter += 2
            j-=1
            
    return counter

a = [9,8,7,6,5]


print("unsorted list:", a)
print("number of memory write operations:", inssort(a))
print("sorted list:", a)
