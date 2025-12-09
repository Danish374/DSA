from collections import Counter

class Solution:
    def specialTriplets(self, nums: list[int]) -> int:
        left = Counter()
        right = Counter(nums)
        res = 0
        MOD = 10**9 + 7
        
        for x in nums:
            right[x] -= 1
            target = 2 * x
            res = (res + left[target] * right[target]) % MOD
            left[x] += 1
        
        return res
