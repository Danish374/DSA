class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        int prev[n], curr[n];  
        memset(prev, 0, sizeof(prev));
        memset(curr, 0, sizeof(curr));

        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 1) {
                    if (i == 0 || j == 0) {
                        curr[j] = 1;
                    } else {
                        curr[j] = 1 + min({prev[j], curr[j-1], prev[j-1]});
                    }
                    ans += curr[j];
                } else {
                    curr[j] = 0;
                }
            }
            memcpy(prev, curr, sizeof(curr)); // move curr → prev
        }
        return ans;
    }
};
