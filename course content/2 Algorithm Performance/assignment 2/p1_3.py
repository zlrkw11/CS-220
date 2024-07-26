a = [1,2,3]
n = len(a)
count = 0
def sifynia(n):
    for i in range(1, n/2+1):
        a[2*i-1] = 3*i
        a[2*i] = i-1
        count+=1
    for i in range(1, n+1):
        if a[i] == n:
            return 
        count+=1
    print(count)
    