n = 2
i = 0
f = 1
count = 0
while f < n**n:
    i+=1
    f=f*i
    count += 1

print(count)