a = [5,2,9,1,6]

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
    temp = []
    while len(a)>j:
        temp.append(a.pop())
    a.append(t)
    while temp:
        a.append(temp.pop())

def erase(a, i):
    # [5,2,9,1,6] -> [2,5,9,1,6]
    temp = []
    while len(a) > i+1:
        temp.append(a.pop())
    removed_item = a.pop()
    for i in range(len(temp)):
        a.append(temp.pop())
    return removed_item


inssort(a)
print(a)
    
