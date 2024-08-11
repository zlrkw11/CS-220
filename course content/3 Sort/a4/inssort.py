a = [3,4,5]

def inssort(a):
    n = len(a)
    for i in range(1, n):
        j = i - 1
        while j >= 0 and a[i] < a[j]:
            j -= 1
        j += 1
        if j < i:
            t = erase(a, i)
            insert(a, j, t)

def insert(a, j, t):
    pass

def erase(a, i):
    pass
