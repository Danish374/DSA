class Solution {
public:
    vector<string> spellchecker(vector<string>& wordlist, vector<string>& queries) {
        unordered_set<string> exact(wordlist.begin(), wordlist.end());
        unordered_map<string, string> caseMap;
        unordered_map<string, string> vowelMap;

        for (auto& w : wordlist) {
            string lower = toLower(w);
            if (!caseMap.count(lower)) caseMap[lower] = w;
            string dev = devowel(lower);
            if (!vowelMap.count(dev)) vowelMap[dev] = w;
        }

        vector<string> ans;
        for (auto& q : queries) {
            if (exact.count(q)) ans.push_back(q);
            else {
                string lower = toLower(q);
                if (caseMap.count(lower)) ans.push_back(caseMap[lower]);
                else {
                    string dev = devowel(lower);
                    if (vowelMap.count(dev)) ans.push_back(vowelMap[dev]);
                    else ans.push_back("");
                }
            }
        }
        return ans;
    }

private:
    string toLower(const string& s) {
        string t = s;
        for (auto& c : t) c = tolower(c);
        return t;
    }

    string devowel(const string& s) {
        string t = s;
        for (auto& c : t) {
            if (c=='a'||c=='e'||c=='i'||c=='o'||c=='u') c = '*';
        }
        return t;
    }
};
