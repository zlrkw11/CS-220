from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r] > target:
                print(numbers[l], numbers[r])
                r -= 1
            elif numbers[l]+numbers[r] < target:
                print(numbers[l], numbers[r])
                l+=1
            else:
                return [l+1,r+1]

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
print(solution.twoSum([2,3,4], 6))
print(solution.twoSum([-1,0], -1))