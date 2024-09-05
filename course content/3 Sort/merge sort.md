# Merge Sort
## Algorithm:

````
Function MergeSort(l, h):
    if (l < h):
        mid = (l + h)/2
        MergeSort(l, mid)
        MergeSort(mid+1, h)
        Merge(l, mid, h)
````

## Example:
[9,3,7,5,6,4,8,2]

pass index 1,8 as low and high

            1,8
        1,4     5,8
     1,2   3,4

break elements into 2 lists
until into 2 elements in every group, then merge 2
then merge groups together until there is 1 final merged group consists of n elements.

