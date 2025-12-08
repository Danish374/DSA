class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c2 = a * a + b * b
                c = int(c2**0.5)
                if c * c == c2 and c <= n:
                    ans += 1
        return ans
