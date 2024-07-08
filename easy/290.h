#include "../stdc++.h"
using namespace std;

class Solution {
public:
    bool wordPattern(string pattern, string s) {
        vector<string> t;
        string tmp = "";

        for(int i = 0; i < s.size(); i++){
            if(s[i] == ' '){
                t.push_back(tmp);
                tmp = "";
            } else{
                tmp += s[i];
            }
        }
        t.push_back(tmp);

        if(pattern.size() != t.size()) return false;

        unordered_map<char, string> um;
        unordered_map<string, char> um2;

        for(int i = 0; i < pattern.size(); i++){
            if(um.count(pattern[i])){
                if(um[pattern[i]] != t[i]) return false;
            } else{
                um[pattern[i]] = t[i];
            }

            if(um2.count(t[i])){
                if(um2[t[i]] != pattern[i]) return false;
            } else{
                um2[t[i]]= pattern[i];
            }
        }
        return true;
    }
};