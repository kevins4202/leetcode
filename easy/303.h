#include "../stdc++.h"
using namespace std;

class NumArray {
public:
    vector<int> pf;
    NumArray(vector<int>& nums) {
        pf.push_back(0);
        for(int x : nums){
            pf.push_back(x + pf.back());
        }
    }
    
    int sumRange(int left, int right) {
        return pf[right+1] - pf[left];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */