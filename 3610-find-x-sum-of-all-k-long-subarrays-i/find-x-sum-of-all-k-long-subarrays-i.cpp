class Solution {
public:
    vector<int> findXSum(vector<int>& nums, int k, int x) {
        vector<int> res;
        unordered_map<int,int> freq;
        for (int i = 0; i < k; i++) freq[nums[i]]++;
        for (int i = 0; i + k <= nums.size(); i++) {
            if (i > 0) {
                int left = nums[i - 1], right = nums[i + k - 1];
                if (--freq[left] == 0) freq.erase(left);
                freq[right]++;
            }
            vector<pair<int,int>> v(freq.begin(), freq.end());
            sort(v.begin(), v.end(), [](auto& a, auto& b) {
                return a.second == b.second ? a.first > b.first : a.second > b.second;
            });
            long long sum = 0;
            for (int j = 0; j < x && j < v.size(); j++)
                sum += 1LL * v[j].first * v[j].second;
            res.push_back(sum);
        }
        return res;
    }
};
