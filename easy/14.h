#include "../stdc++.h"

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string ans;

        int k = 0;

        for(char c : strs[0]){
            for(int i = 1; i < strs.size(); i++) {
                if(c != strs[i][k]) return ans;
            }

            ans += c;
            k++;
        }

        return ans;
    }
};