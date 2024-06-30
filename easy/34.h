#include "../stdc++.h"
using namespace std;

class Solution {
public:
    int strStr(string haystack, string needle) {
        auto it = haystack.find(needle);
        return (it == string::npos) ? -1 : (int) it;
    }
};