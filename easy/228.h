#include "../stdc++.h"
using namespace std;

class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> ans;
        if(nums.size() == 0) return ans;
        if(nums.size() == 1) return {to_string(nums[0])};

        int left = nums[0];
        int right = left;

        for(int i = 1; i < nums.size(); i++){
            if(nums[i] != nums[i-1] + 1){
                if(left == right) ans.push_back(to_string(left));
                else ans.push_back(to_string(left) + "->" + to_string(right));
                left = nums[i];
                right = left;
            }

            right = nums[i];
        }

        if(nums[nums.size() - 1] == nums[nums.size() - 2] + 1) {
            ans.push_back(to_string(left) + "->" + to_string(right));
        } else{
            ans.push_back(to_string(right));
        }

        return ans;
    }
};