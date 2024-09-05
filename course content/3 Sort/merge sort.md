# Merge Sort
Algorithm:

````
Function MergeSort(l, h):
    if (l < h):
        mid = (l + h)/2
        MergeSort(l, mid)
        MergeSort(mid+1, h)
        Merge(l, mid, h)
````