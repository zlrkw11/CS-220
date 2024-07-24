## Algorithm performance

### calculating running time:

https://www.youtube.com/watch?v=_t2GVaQasRY&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12

running time adds for disjoint blocks.

## Loop 1 example

for every value of i, we run through ALL values of j before go to the next value of i. So, the total amount of work looks like `Cn^3`

```
j i
1 1 ... n
.
.
.
n^2
```

the big picture: for independent nested loop, the running time _multiply_, up to a constant.

## Swap 1 example

this is a constant time algorithm because the running time is _independent_ of n (input size)

## Exponential - Power of 2

i keeps growing until it is equal to n. And we have k iterations up to that point. If we have k iterations, the last iteration is k-1 as we started with power 0.

```
i <- 1 (2^0)
i <- 2 (2^1)
i <- 3 (2^2)
i <- 4 (2^3)
i <- 5 (2^4)
i <- 6 (2^5)
...
i <- n (2^k-1)
```

```
2^k-1 <= n < 2^k
k-1 <= log n < k
```

k-1 is the biggest integer we can reach, power of k will be too big. So, the biggest integer (k-1) less or equal to something (n) is called floor.
so,

```
k-1 = floor(log n)
k = 1 + floor(log n)
```

what's important is that k is roughly log n.

## Nested loops
