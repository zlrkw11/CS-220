# given a list of strings, check if they are anagrams

# 2 strings are anagrams if we SORT them (tan) (nat) -> (ant)
# time: O(m * nlogn)

# instead, count the number of alphabets each word has, record with a hashmap
# [1e, 1a, 1t] = ['eat'], ['ate'], ['tea']
# O(m * n * 26) = O(m * n)

from sklearn.base import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping the charCount to list of anagrams
        for s in strs:
            count = [0] * 26 # a..z

            for c in s:
                count[ord(c) - ord("a")] += 1 # find the c using ascii, increment
            
            res[tuple(count)].append(s) # list cannot be keys
        return res.values()
