from typing import List 
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        i = 0
        while i < len(nums):
            if len(nums) == 0:
                return count 
            first = nums[i]
            p = k-first
            if p not in nums[i::]:
                i+=1
            else:
                nums.remove(first)
                nums.remove(p)
                count+=1
                i = 0
        return count
solution = Solution()
print(solution.maxOperations([4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4],2))
print(solution.maxOperations([1,2,3,4],5))
print(solution.maxOperations([3,1,3,4,3],6))