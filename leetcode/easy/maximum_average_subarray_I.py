from typing import List 
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        ans = s = sum(nums[:k])
        for i in range(k, n):
            s += nums[i] - nums[i-k]
            ans = max(ans, s)
        return ans/k
        
solution = Solution()
print(solution.findMaxAverage([1,12,-5,-6,50,3], 4))