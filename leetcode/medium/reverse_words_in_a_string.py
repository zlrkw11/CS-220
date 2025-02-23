class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])

solution = Solution()
print(solution.reverseWords("hello world"))
        