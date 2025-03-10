# O(n) O(1)
# [1,2,3,1]
from typing import List 
class Solution:
    def rob(self, nums:List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        first = nums[0]
        back = 0
        for i in range(1, n):
            res = max(nums[i] + back, first)
            back = first
            first = res

        return res
solution = Solution()
print(solution.rob([1,2,3,1]))