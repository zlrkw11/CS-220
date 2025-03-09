from typing import List 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high-low) // 2
            if nums[mid] == target:
                return mid
            elif mid < target:
                low = mid+1
            else:
                high = mid-1            
        return -1

solution = Solution()
print(solution.search([-1,0,2,4,6,8], 4))