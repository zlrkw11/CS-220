class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
    
        l = len([flower for flower in flowerbed if flower == 0])
        if (l == n * 2 + 1):
            return True
        return False
        
        
solution = Solution()
print(solution.canPlaceFlowers([1,0,0,0,0,1], 1))
print(solution.canPlaceFlowers([1,0,0,0,1], 1))