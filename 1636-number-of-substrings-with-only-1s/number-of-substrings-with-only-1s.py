class Solution:
    def numSub(self, s: str) -> int:
        ans = 0
        cnt = 0
        mod = 10**9 + 7
        for c in s:
            if c == '1':
                cnt += 1
                ans = (ans + cnt) % mod
            else:
                cnt = 0
        return ans
