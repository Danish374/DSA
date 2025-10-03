import heapq

class Solution:
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []

        for i in range(m):
            for j in (0, n - 1):
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        for j in range(n):
            for i in (0, m - 1):
                if not visited[i][j]:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        res = 0
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        max_height = 0

        while heap:
            h, x, y = heapq.heappop(heap)
            max_height = max(max_height, h)
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    nh = heightMap[nx][ny]
                    if nh < max_height:
                        res += max_height - nh
                    heapq.heappush(heap, (max(nh, max_height), nx, ny))

        return res
