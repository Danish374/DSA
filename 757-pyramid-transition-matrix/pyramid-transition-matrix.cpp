class Solution {
public:
    unordered_map<string, vector<char>> mp;
    unordered_map<string, bool> memo;

    bool dfs(const string& bottom) {
        if (bottom.size() == 1) return true;
        if (memo.count(bottom)) return memo[bottom];

        int n = bottom.size();
        vector<vector<char>> choices(n - 1);

        for (int i = 0; i < n - 1; i++) {
            string key = bottom.substr(i, 2);
            if (!mp.count(key)) return memo[bottom] = false;
            choices[i] = mp[key];
        }

        function<bool(int, string&)> build = [&](int idx, string& next) {
            if (idx == n - 1) return dfs(next);
            for (char c : choices[idx]) {
                next.push_back(c);
                if (build(idx + 1, next)) return true;
                next.pop_back();
            }
            return false;
        };

        string next = "";
        bool res = build(0, next);
        memo[bottom] = res;
        return res;
    }

    bool pyramidTransition(string bottom, vector<string>& allowed) {
        for (auto& s : allowed)
            mp[s.substr(0, 2)].push_back(s[2]);
        return dfs(bottom);
    }
};
