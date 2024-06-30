#include <iostream>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> m;
        m['I'] = 1;
        m['V'] = 5;
        m['X'] = 10;
        m['L'] = 50;
        m['C'] = 100;
        m['D'] = 500;
        m['M'] = 1000;

        int prev = 10000;
        int ans = 0;

        for (char c : s){
            if(m[c] > prev) {
                ans -= 2 * prev;
            }

            prev = m[c];

            ans += m[c];
        }

        return ans;
    }
};