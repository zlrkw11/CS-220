a = [5,2,9,1,6]

counter = [0]

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
    last = a[len(a)-1]

    for index in range(len(a)-1, j, -1):
        a[index] = a[index-1]

    a.append(last)
    a[j] = t

def erase(a, i):
    temp = a[i]

    for index in range(i, len(a)-1):
        a[index] = a[index+1]
        
    a.pop()
    return temp

inssort(a)
print(a)
