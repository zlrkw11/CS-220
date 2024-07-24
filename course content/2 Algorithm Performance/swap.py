n = 10
arr = list(range(n))
def swap(i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t
    print(arr)
    return arr

swap(1,2)
