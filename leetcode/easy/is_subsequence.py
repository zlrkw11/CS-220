class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = 0
        if len(s)==0:
            return True
        if len(t)==0:
            return False
        if len(s) and len(t):
            for i in range(len(t)):
                if s[p1] == t[i]:
                    p1 += 1
                    if p1 == len(s):
                        return True
            return False
        

solution = Solution()
print(solution.isSubsequence("abc", "ahbgdc"))
print(solution.isSubsequence("b", "abc"))
