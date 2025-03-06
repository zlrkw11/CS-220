class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s, t = ''.join(sorted(s)), ''.join(sorted(t))
        return (s==t)
            
        
solution = Solution()
print(solution.isAnagram("jar", "raj"))
print(solution.isAnagram("jart", "rajm"))