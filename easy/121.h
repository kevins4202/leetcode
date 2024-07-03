#include "../stdc++.h"
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        vector<int> maxs(prices.size());

        maxs[maxs.size() - 1] = prices[prices.size() - 1];

        for(int i = prices.size() - 2; i >= 0; i--){
            maxs[i] = max(maxs[i+1], prices[i]);
        }

        int mn = prices[0];
        int ans = -1000000;
        for(int i = 0; i < prices.size(); i++){
            mn = min(mn, prices[i]);
            ans = max(ans, maxs[i]-mn);
        }

        return ans;
    }
};