from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = 0
        for i in range(len(nums)):
           if nums[i] != 0:
               nums[i], nums[pointer] = nums[pointer], nums[i]
               pointer+=1

nums = [0,1,0,3,12]
solution = Solution()

solution.moveZeroes(nums)
print(nums)