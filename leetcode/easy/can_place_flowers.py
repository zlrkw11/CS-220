class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
    
        if(len(flowerbed) % 2 == n % 2):
            return True
        return False 
        
        
solution = Solution()
print(solution.canPlaceFlowers([1,0,0,0,1], 1))