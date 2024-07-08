#include "../stdc++.h"
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> cnt(128, 0);

        if(s.size() != t.size()) return false;

        for(int i = 0; i < s.size(); i++){
            cnt[s[i]]++;
            cnt[t[i]]--;
        }

        for(int y : cnt) if(y) return false;
        return true;
    }
};