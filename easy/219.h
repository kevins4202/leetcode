#include "../stdc++.h"
using namespace std;


class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> um;

        for(int i = 0; i < nums.size(); i++){
            int x = nums[i];
            if(um.count(x)) {
                if(i - um[x] <= k) return true;
            }

            um[x] = i;
        }

        return false;
    }
};