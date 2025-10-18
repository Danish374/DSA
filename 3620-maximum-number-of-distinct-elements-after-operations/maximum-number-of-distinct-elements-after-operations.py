from typing import List

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        prev = float('-inf')
        for x in nums:
            if prev < x + k:
                cur = max(prev + 1, x - k)
                prev = cur
                ans += 1
        return ans
