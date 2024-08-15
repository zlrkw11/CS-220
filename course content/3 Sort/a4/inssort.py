a = [1,2,3,4,5,6,7]

counter = [0]

def inssort(a, counter):
    n = len(a)
    for i in range(1, n):
        j = i - 1
        while j >= 0 and a[i] < a[j]:
            j -= 1
        j += 1
        if j < i:
            t = erase(a, i, counter)
            insert(a, j, t, counter)

def insert(a, j, t, counter):
    temp = []
    while len(a)>j:
        temp.append(a.pop())
        counter[0] += 1
        
    a.append(t)
    counter[0] += 1
    
    while temp:
        a.append(temp.pop())
        counter[0] += 1

def erase(a, i, counter):
    temp = []
    while len(a) > i+1:
        temp.append(a.pop())
        counter[0] += 1
        
    removed_item = a.pop()
    counter[0] += 1
    
    for i in range(len(temp)):
        a.append(temp.pop())
        counter[0] += 1
        
    return removed_item

print("unsorted list:",a)
inssort(a, counter)
print("number of memory write operations:", counter[0])
print("sorted list:",a)
    
