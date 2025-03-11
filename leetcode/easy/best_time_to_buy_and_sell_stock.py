from math import inf
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, low = 0, inf
        for price in prices:
            ans = max(ans, price-low)
            low = min(price, low)
        return ans