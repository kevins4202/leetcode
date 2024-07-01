#include "../stdc++.h"
using namespace std;

class Solution {
public:
    int lengthOfLastWord(string s) {
        int j = s.size() - 1;

        // while(i < s.size() && s[i] == ' ') i++;
        while(j >= 0 && s[j] == ' ') j--;
        int i = j;
        while(i >= 0 && s[i] != ' ') i--;

        if(i == 0 && s[i] != ' ') i--;

        return j - i;
    }
};