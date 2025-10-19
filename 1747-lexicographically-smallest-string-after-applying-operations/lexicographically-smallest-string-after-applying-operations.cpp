class Solution {
public:
    string findLexSmallestString(string s, int a, int b) {
        string ans = s;
        int n = s.size();
        queue<string> q;
        unordered_set<string> seen;
        q.push(s);
        seen.insert(s);

        while (!q.empty()) {
            string cur = q.front();
            q.pop();
            if (cur < ans) ans = cur;

            string t1 = cur;
            for (int i = 1; i < n; i += 2) {
                t1[i] = char('0' + ( (t1[i] - '0' + a) % 10 ));
            }
            if (!seen.count(t1)) {
                seen.insert(t1);
                q.push(t1);
            }

            string t2 = cur.substr(n - b) + cur.substr(0, n - b);
            if (!seen.count(t2)) {
                seen.insert(t2);
                q.push(t2);
            }
        }

        return ans;
    }
};