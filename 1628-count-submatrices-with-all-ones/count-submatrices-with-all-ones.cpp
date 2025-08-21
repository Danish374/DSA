class Solution {
public:
    int numSubmat(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        vector<int> height(n, 0);
        int ans = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 0) height[j] = 0;
                else height[j]++;
            }

            stack<pair<int,int>> st;
            int sum = 0;
            for (int j = 0; j < n; j++) {
                int cnt = 1;
                while (!st.empty() && st.top().first >= height[j]) {
                    sum -= st.top().first * st.top().second;
                    cnt += st.top().second;
                    st.pop();
                }
                st.push({height[j], cnt});
                sum += height[j] * cnt;
                ans += sum;
            }
        }
        return ans;
    }
};
