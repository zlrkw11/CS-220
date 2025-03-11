from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target:int)-> bool: 
        
        low, high = 0, len(matrix)-1

        while low <= high:
            mid1 = low + (high-low)//2

            if matrix[mid1][0] == target:
                return True
            elif matrix[mid1][0] < target and matrix[mid1][-1] < target:
                low = mid1+1
            elif matrix[mid1][0] > target:
                high = mid1-1
            else:
                break
        
        arr = matrix[mid1]
        low, high = 0, len(arr)-1

        while low <= high:
            mid2 = low + (high-low)//2
            if arr[mid2] == target:
                return True
            elif arr[mid2] < target:
                low = mid2+1
            else:
                high = mid2-1

        return False

solution = Solution()

print(solution.searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 3))

print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 11))