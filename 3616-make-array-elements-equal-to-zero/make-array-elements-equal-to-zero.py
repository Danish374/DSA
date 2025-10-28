from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total = sum(nums)
        ans = 0
        left_sum = 0
        
        for x in nums:
            if x != 0:
                left_sum += x
            else:
                if left_sum * 2 == total:
                    ans += 2
                elif abs(left_sum * 2 - total) == 1:
                    ans += 1
        
        return ans
