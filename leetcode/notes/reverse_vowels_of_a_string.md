
## solution 1
double pointer

```
vowels = "aeiouAEIOU"
        i, j = 0, len(s) - 1
        cs = list(s)
        while i < j:
            while i < j and cs[i] not in vowels:
                i += 1
            while i < j and cs[j] not in vowels:
                j -= 1
            if i < j:
                cs[i], cs[j] = cs[j], cs[i]
                i, j = i + 1, j - 1
        return "".join(cs)
```

repeatedly check for both i and j, 
if either i or j is not a vowel, go to the next i or j
if they didnt cross, see 2 vowels, switch their positions.
