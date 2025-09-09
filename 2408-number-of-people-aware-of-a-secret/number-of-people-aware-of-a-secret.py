class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        
        for day in range(1, n + 1):
            for share in range(day + delay, min(n, day + forget - 1) + 1):
                dp[share] = (dp[share] + dp[day]) % MOD
        
        ans = 0
        for day in range(n - forget + 1, n + 1):
            ans = (ans + dp[day]) % MOD
        return ans
