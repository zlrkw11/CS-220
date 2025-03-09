from typing import List 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + high // 2
            if mid == target:
                return mid
            elif mid < target:
                low = mid+1
            else:
                high = mid-1            
        return False

solution = Solution()
print(solution.search([]))