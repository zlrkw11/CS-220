
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"()","[]","{}"}
        for c in s:
            if c in "([{":
                stack.append(c)
            elif not stack or stack.pop()+c not in d:
                return False
        return not stack
    

solution = Solution()
print(solution.isValid("[][][]"))