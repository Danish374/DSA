class Solution:
    def maxKDivisibleComponents(self, n: int, edges: list[list[int]], values: list[int], k: int) -> int:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        ans = 0

        def dfs(u, parent):
            nonlocal ans
            s = values[u]
            for v in g[u]:
                if v == parent:
                    continue
                s += dfs(v, u)
            if s % k == 0:
                ans += 1
                return 0
            return s

        dfs(0, -1)
        return ans
