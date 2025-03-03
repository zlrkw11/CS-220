from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = nums.sort()
        l, r = nums[0], len(nums)-1
        ans = 0
        s = nums[l] + nums[r]
        while l < r:
            if s == k:
                ans += 1
                l, k = l+1, k+1
            elif s < k:
                l += 1
            else:
                r += 1
        return ans
solution = Solution()
print(solution.maxOperations())