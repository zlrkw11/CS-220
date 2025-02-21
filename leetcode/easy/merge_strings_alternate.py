class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        final_string = ""
        len1, len2 = len(word1), len(word2)
        for i in range(max(len1, len2)):
            if i < len1:
                final_string += word1[i]
            if i < len2:
                final_string += word2[i]
        return final_string

# 创建 Solution 类的实例
solution = Solution()
# 调用 mergeAlternately 方法并打印结果
print(solution.mergeAlternately("ab", "pqrs"))