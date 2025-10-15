class Solution {
public:
    int maxIncreasingSubarrays(vector<int>& nums) {
        int n = nums.size();
        if (n < 2) return 0;

        vector<int> inc(n, 1);
        for (int i = 1; i < n; ++i) {
            if (nums[i] > nums[i-1]) inc[i] = inc[i-1] + 1;
            else inc[i] = 1;
        }

        auto possible = [&](int k) -> bool {
            if (k == 0) return true;
            if (2*k > n) return false;
            for (int i = 2*k - 1; i < n; ++i) {
                if (inc[i] >= k && inc[i - k] >= k) return true;
            }
            return false;
        };

        int lo = 0, hi = n / 2, ans = 0;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (possible(mid)) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return ans;
    }
};
