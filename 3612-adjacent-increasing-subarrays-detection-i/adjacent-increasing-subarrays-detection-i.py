from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        mx = 0
        prev = 0
        cur = 0
        n = len(nums)

        for i, x in enumerate(nums):
            cur += 1
            if i == n - 1 or x >= nums[i + 1]:
                mx = max(mx, cur // 2, min(prev, cur))
                prev = cur
                cur = 0

        return mx >= k
