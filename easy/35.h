#include "../stdc++.h"
using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int lo = 0;
        int hi = nums.size() - 1;
        int mid;

        while(lo <= hi){
            int mid = lo + (hi - lo) / 2;
            // cout<<mid<<endl;

            if(nums[mid] > target) hi = mid - 1;
            else if(nums[mid] < target) lo = mid + 1;
            else return mid;
        }

        return lo;
    }
};