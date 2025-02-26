class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        if all(num==0 for num in nums):
            return [0]*len(nums)
        for i in range(len(nums)):
            o = [n for n in nums if n != nums[i]]
            p = 1
            for j in o:
                p *= j
            arr.append(p)
        return arr

solution = Solution()
print(solution.productExceptSelf([0,0]))


