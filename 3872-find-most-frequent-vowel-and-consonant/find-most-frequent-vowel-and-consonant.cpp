class Solution {
public:
    int maxFreqSum(string s) {
        int freq[26] = {0};
        for (char c : s) {
            freq[c - 'a']++;
        }
        
        int maxV = 0, maxC = 0;
        auto isVowel = [&](char c) {
            return c=='a' || c=='e' || c=='i' || c=='o' || c=='u';
        };
        
        for (int i = 0; i < 26; i++) {
            char c = 'a' + i;
            if (isVowel(c)) {
                maxV = max(maxV, freq[i]);
            } else {
                maxC = max(maxC, freq[i]);
            }
        }
        return maxV + maxC;
    }
};
