class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9 + 7
        aba = 6
        abc = 6

        for _ in range(2, n + 1):
            new_aba = (aba * 3 + abc * 2) % mod
            new_abc = (aba * 2 + abc * 2) % mod
            aba, abc = new_aba, new_abc

        return (aba + abc) % mod
