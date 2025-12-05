class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        total = sum(nums)
        prefix = 0
        ans = 0

        for i in range(len(nums) - 1):
            prefix += nums[i]
            if (prefix - (total - prefix)) % 2 == 0:
                ans += 1

        return ans
