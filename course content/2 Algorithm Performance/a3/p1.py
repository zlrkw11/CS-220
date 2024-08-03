a = [1,0,0,1]
def eastylat(a):
    counter = 0
    n = len(a)
    s = 0
    for i in range(0, n):
        s += a[i]
        counter += 1
    for i in range(s):
        counter += 1

    return counter

print(eastylat(a))