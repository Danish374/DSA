class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        if (mat.empty()) return {};
        
        int m = mat.size(), n = mat[0].size();
        vector<int> result;
        result.reserve(m * n);
        
        for (int d = 0; d < m + n - 1; d++) {
            int r, c;
            if (d % 2 == 0) {
                r = (d < m) ? d : m - 1;
                c = d - r;
                while (r >= 0 && c < n) {
                    result.push_back(mat[r][c]);
                    r--, c++;
                }
            } else {
                c = (d < n) ? d : n - 1;
                r = d - c;
                while (c >= 0 && r < m) {
                    result.push_back(mat[r][c]);
                    r++, c--;
                }
            }
        }
        return result;
    }
};
