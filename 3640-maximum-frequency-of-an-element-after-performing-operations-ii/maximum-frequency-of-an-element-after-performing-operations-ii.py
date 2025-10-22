from typing import List
from collections import Counter

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        count = Counter(nums)
        diff = Counter()

        for v in nums:
            diff[v - k] += 1
            diff[v + k + 1] -= 1

        keys = sorted(set(diff.keys()) | set(count.keys()))
        ans = 0
        curr = 0
        idx = 0
        diffs = sorted(diff.items())

        for x in keys:
            while idx < len(diffs) and diffs[idx][0] <= x:
                curr += diffs[idx][1]
                idx += 1
            already = count.get(x, 0)
            possible = min(curr, already + numOperations)
            ans = max(ans, possible)
        return ans
