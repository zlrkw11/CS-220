class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = []
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                if [k for k in strs[i]].sort() == [h for h in strs[j]].sort():
                    n += [strs[i], strs[j]]
        return n