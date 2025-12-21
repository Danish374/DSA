class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        res = 0
        sorted_rows = [False] * (n - 1)

        for col in range(m):
            bad = False
            for i in range(n - 1):
                if not sorted_rows[i] and strs[i][col] > strs[i + 1][col]:
                    bad = True
                    break
            if bad:
                res += 1
            else:
                for i in range(n - 1):
                    if strs[i][col] < strs[i + 1][col]:
                        sorted_rows[i] = True
        return res
