#include "../stdc++.h"
using namespace std;

class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> ans(n+1, 0);

        if (n == 0) return ans;

        ans[1] = 1;

        int p = 1;
        int tail = 1;

        for(int i = 2; i < n+1; i++){
            if(2 * p == i) {
                ans[i] = 1;
                tail = 1;
                p *= 2;
            } else {
                ans[i] = 1 + ans[tail];
                tail++;
            }
        }

        return ans;
        
    }
};