# Asymptotic Notation

## 3 notations

1 < logn < sqrt(n) < n < nlogn < n^2 < n^3 ... < 2^n < 3^n < ... n^n 
### big O
The function f(n) = O(g(n)) if and only if there exists positive constants **C & N0** such that f(n) <= C*g(n) for all n greater than N0.

example:
f(n) = 2n+3
2n+3 <= 10n
f(n) <= C*g(n)

so, f(n) is O(g(n))

anything on the right of the chart of runtime complexity will be an upper bound of f(n), anything left will be a lower bound. n will be an avg bound.

### big Omega
The function f(n) is big omega of g(n) if and only if there exists a positive constant **C and N0** such that f(n) >= C*g(n) for all n >= n0.
### theta

