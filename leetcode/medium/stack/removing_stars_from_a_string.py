from typing import List
class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for c in s:
            if c=="*":
                ans.pop()
            else:
                ans.append(c)
        return ''.join(ans)
# "*"

solution = Solution()
print(solution.removeStars("leet**cod*e"))