class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        i = 0
        while i < len(flowerbed):
            print(flowerbed)
            if i == 0:
                if flowerbed[1] != 1:
                    n-=1 
                    flowerbed[0] = 1
                i+=1
            else:
                if not (flowerbed[i] == 1 and flowerbed[i-1] == 1 and flowerbed[i+1] == 1):
                    flowerbed[i] = 1
                    n-=1
                i += 1
        return n==0
             
        
        
solution = Solution()
print(solution.canPlaceFlowers([1,0,0,0,0,1], 2))
print(solution.canPlaceFlowers([1,0,0,0,1], 1))