class Solution {
public:
    vector<int> replaceNonCoprimes(vector<int>& nums) {
        vector<int> stk;
        for (int x : nums) {
            stk.push_back(x);
            while (stk.size() > 1) {
                long long a = stk.back();
                long long b = stk[stk.size() - 2];
                int g = gcd(a, b);
                if (g == 1) break;
                stk.pop_back();
                long long l = a / g * b;
                stk.back() = (int)l;
            }
        }
        return stk;
    }

private:
    int gcd(long long a, long long b) {
        while (b != 0) {
            long long t = a % b;
            a = b;
            b = t;
        }
        return (int)a;
    }
};
