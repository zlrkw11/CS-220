a = [1,2,3,4]
n = len(a)
print(n)

def sifynia(n):
    count = 0
    for i in range(1, int(n/2)+1):
        a[2*i-1] = 3*i
        a[2*i] = i-1
        count+=1
    for i in range(1, n+1):
        if a[i] == n:
            return 
        count+=1
    print(count)

sifynia(n)