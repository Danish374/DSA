#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> productQueries(int n, vector<vector<int>>& queries) {
        const int MOD = 1e9 + 7;
        vector<int> powers;
        
        for (int i = 0; n > 0; i++) {
            if (n & 1) powers.push_back(1 << i);
            n >>= 1;
        }
        
        vector<long long> prefix(powers.size() + 1, 1);
        for (int i = 0; i < powers.size(); i++) {
            prefix[i + 1] = (prefix[i] * powers[i]) % MOD;
        }
        
        vector<int> ans;
        for (auto &q : queries) {
            int l = q[0], r = q[1];
            long long prod = prefix[r + 1] * modInverse(prefix[l], MOD) % MOD;
            ans.push_back((int)prod);
        }
        
        return ans;
    }

private:
    long long modPow(long long a, long long b, int m) {
        long long res = 1;
        while (b > 0) {
            if (b & 1) res = (res * a) % m;
            a = (a * a) % m;
            b >>= 1;
        }
        return res;
    }

    long long modInverse(long long a, int m) {
        return modPow(a, m - 2, m); // Fermat's Little Theorem
    }
};
