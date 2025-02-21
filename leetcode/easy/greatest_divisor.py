class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len1, len2 = len(str1), len(str2)

        def valid(k):
            if len1 % k or len2 % k:
                return False
            n1, n2 = len1//k, len2//k
            base = str1[:k]
            return str1 == n1 * base and str2 == n2 * base
        
        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i]
    
solution = Solution()
print(solution.gcdOfStrings("ABCABC", "ABC"))