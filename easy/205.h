#include "../stdc++.h"
using namespace std;

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> m1, m2;

        for(int i = 0; i < s.size(); i++){
            char ss = s[i];
            char tt = t[i];

            if(m1.count(ss)) {
                if(m1[ss] != tt) return false;
            }
            else {
                m1[ss] = tt;
            }

            if(m2.count(tt)) {
                if(m2[tt] != ss) return false;
            }
            else {
                m2[tt] = ss;
            }

        }   

        return true;     
    }
};