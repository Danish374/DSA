class Solution {
public:
    bool reorderedPowerOf2(int n) {
        int cnt = encode(n);
        for (int i = 0; i < 31; ++i) {
            if (encode(1 << i) == cnt) return true;
        }
        return false;
    }

private:
    int encode(int x) {
        int count = 0;
        while (x > 0) {
            count += pow(10, x % 10);
            x /= 10;
        }
        return count;
    }
};
