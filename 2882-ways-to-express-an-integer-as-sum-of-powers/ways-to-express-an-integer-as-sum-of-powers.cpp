class Solution {
public:
    int numberOfWays(int n, int x) {
        const int MOD = 1'000'000'007;
        vector<int> dp(n + 1, 0);
        dp[0] = 1;

        for (int a = 1; ; ++a) {
            long power = 1;
            for (int i = 0; i < x; ++i) power *= a;
            if (power > n) break;
            
            int p = (int)power;
            for (int i = n; i >= p; --i) {
                dp[i] = (dp[i] + dp[i - p]) % MOD;
            }
        }

        return dp[n];
    }
};
