#include "../stdc++.h"
using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i = 0;
        int j = 0;
        for(; j < nums.size(); j++){
            if(nums[j] != 0){
                nums[i] = nums[j];
                i++;
            }
        }

        for(; i < nums.size(); i++){
            nums[i] = 0;
        }
    }
};