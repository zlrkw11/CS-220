
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
        
            stack.append(c)
            
            stack.pop()
        return len(stack)==0
    

solution = Solution()
print(solution.isValid("([{}])"))