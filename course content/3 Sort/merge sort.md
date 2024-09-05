# Merge Sort
## Algorithm:

*note low and high are indices
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
  1,1 2,2 3,3 4,4

break elements into 2 lists
until into 2 elements in every group, then merge 2
then merge groups together until there is 1 final merged group consists of n elements.

## Running Time
n elements are merged 
3 levels for 8 elements.
which is 
````
n * log(n)
````

## Procedure
ORG Array: [9,3,7,5,6,4,8,2]

1 ~ 4
[9,3,7,5]

1 ~ 2   3 ~ 4
[9,3]   [5,7]

1
[9]

2
[3]

3
[7]

4
[5]

we now have 4 elements separated, we merge. Which re-arranges the order and merge the 4 small lists into 1: [3,5,7,9].

same goes for the other list:
we get [6] [4] [8] [2]
call merge function and we get [2,4,6,8].