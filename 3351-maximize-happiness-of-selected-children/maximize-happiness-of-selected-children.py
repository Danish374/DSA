class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort(reverse=True)
        ans = 0
        for i in range(k):
            val = max(0, happiness[i] - i)
            ans += val
        return ans
