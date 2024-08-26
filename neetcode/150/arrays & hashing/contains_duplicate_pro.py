# brute forcing
# O(n) for every number, 2 numbers 
# O(n^2) total for time

# O(1), no extra space

# we can sort the array 
# check 2 neighbours, so time will be O(n log n), O(1) for space


# or use a hashset
# time: O(n), space: O(n)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            
            hashset.add(n)

        return False