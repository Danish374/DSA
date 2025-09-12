class Solution {
public:
    bool doesAliceWin(string s) {
        for (char c : s) {
            if (isVowel(c)) return true;
        }
        return false;
    }

private:
    bool isVowel(char c) {
        static string vowels = "aeiou";
        for (char v : vowels) {
            if (c == v) return true;
        }
        return false;
    }
};
