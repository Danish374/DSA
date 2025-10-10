from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        largest_indices = sorted(range(len(nums)), key=lambda i: nums[i], reverse=True)[:k]
        largest_indices.sort()
        return [nums[i] for i in largest_indices]
