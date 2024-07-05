#include "../stdc++.h"
using namespace std;

class Solution {
public:
    int titleToNumber(string s) {
        int ans = 0;
        long pow = 1;

        reverse(s.begin(), s.end());

        for(char x : s){
            ans += pow * (x - 'A' + 1);
            pow *= 26;
        }

        return ans;
    }
};