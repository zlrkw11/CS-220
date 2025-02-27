class Solution(object):
    def compress(self, chars):
        s=[]
        j = 1
        if len(chars) == 1:
            s = [chars[0], '1']
            return s
        for j in range(len(chars)):
            if chars[j] != chars[j-1]:
                c, count = self.counter(chars, j)
                s.append(c)
                s.append(count)
        return s

    def counter(self, chars, i):
        count = 0
        c = chars[i]
        while i < len(chars):
            if chars[i] == c:
                count += 1
            i += 1
        if count > 9:
            return list(str(count))
        return c, str(count)

solution = Solution()
print(solution.compress(['a', 'a', 'a', 'b', 'b']))
print(solution.compress(["a","a","b","b","c","c","c"]))
print(solution.compress(['a']))
print(solution.compress(['a','b','b']))