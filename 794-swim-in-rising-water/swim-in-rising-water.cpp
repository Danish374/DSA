class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<vector<int>> visited(n, vector<int>(n, 0));
        priority_queue<array<int, 3>, vector<array<int, 3>>, greater<>> pq;
        
        pq.push({grid[0][0], 0, 0});
        visited[0][0] = 1;
        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        
        while (!pq.empty()) {
            auto [t, x, y] = pq.top();
            pq.pop();
            
            if (x == n - 1 && y == n - 1) return t;
            
            for (auto& d : dirs) {
                int nx = x + d[0], ny = y + d[1];
                if (nx >= 0 && ny >= 0 && nx < n && ny < n && !visited[nx][ny]) {
                    visited[nx][ny] = 1;
                    pq.push({max(t, grid[nx][ny]), nx, ny});
                }
            }
        }
        return -1;
    }
};
