class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums), 1):
                if nums[j] > nums[i]:
                    for k in range(j+1, len(nums), 1):
                        if (nums[k] > nums[j]):
                            return True
            
        return False

        
solution = Solution()
print(solution.increasingTriplet([20,100,10,12,5,13]))
print(solution.increasingTriplet([1,100,210,312,5,13]))