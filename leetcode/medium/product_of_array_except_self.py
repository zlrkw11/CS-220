class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for i in range(len(nums)):
            o = [n for n in nums if n != nums[i]]
            p = 1
            for j in o:
                p *= j
            arr.append(p)
        return arr

solution = Solution()
print(solution.productExceptSelf([-1,1,0,-3,3]))


