def findmax(a):
    n = len(a)
    imax = 0 # where the current max index is
    for i in range(n):
        if a[i] > a[imax]:
            imax = i
    return imax

def selsort(a):
    n = len(a)
    # iterate from the back of the list
    for i in reversed(range(n)):
        # a[0..i] unsorted
        # a[i] will become sorted
        j = findmax(a[:i+1])
        
        # swap
        a[i], a[j] = a[j], a[i]
    return a


b = [1,5,7,2,4,8]
print(b)
print(selsort(b))

