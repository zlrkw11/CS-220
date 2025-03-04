from typing import List 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            d[nums[i]] += 1
        sorted_keys = sorted(d, key=lambda k:d[k], reverse=True)
        return sorted([sorted_keys[i] for i in range(k)])
             
solution = Solution()
print(solution.topKFrequent([1,2,2,3,3,3], 2))