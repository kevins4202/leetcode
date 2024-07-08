#include "../stdc++.h"
using namespace std;

class Solution {
public:
    string reverseVowels(string s) {
        int lo = 0, hi = s.size() - 1;

        char vowels[10] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        bool isVowel[128];

        for(char c : vowels) isVowel[c] = true;

        while(lo < hi){
            if(isVowel[s[lo]] && isVowel[s[hi]]){
                swap(s[lo], s[hi]);
                lo++; hi--;
            }
            while(lo < s.size() - 1 && !isVowel[s[lo]]) lo++;
            while(hi >= 0 && !isVowel[s[hi]]) hi--;
        }
        
        return s;
    }
};