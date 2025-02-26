class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [0] * n
        left = right = 1
        for i, x in enumerate(nums):
            ans[i] = left
            left *= x
        for i in range(n - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        return ans

solution = Solution()
print(solution.productExceptSelf([4,0,4]))