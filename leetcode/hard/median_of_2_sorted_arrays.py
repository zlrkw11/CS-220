class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        arr = []*(len(nums1)+len(nums2))
        minimum = min(len(nums1), len(nums2))
        x = 0
        y = 0 
        while True:
            if x == len(nums1): 
                arr += nums2[y::]
                break
            elif y == len(nums2):
                arr += nums1[x::]
                break
    
            if nums1[x] <= nums2[y]:
                arr.append(nums1[x])
                x += 1
            else:
                arr.append(nums2[y])
                y += 1
           
        if len(arr) % 2 == 1:
            return arr[len(arr)//2]

        return float((arr[len(arr)//2] + arr[len(arr)//2 -1]) / 2)
    
solution = Solution()
print(solution.findMedianSortedArrays([1,2,3], [4,5,6]))
