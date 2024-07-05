#include "../stdc++.h"
using namespace std;

class Solution {
public:
    
    string convertToTitle(int n) {
        string ans;

        while(n > 0){
            n--;
            int curr = n % 26;
            n/=26;
            ans+= ('A' + curr);
        }

        reverse(ans.begin(), ans.end());
        return ans;


    }
};