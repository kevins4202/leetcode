#include "../stdc++.h"
using namespace std;

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        bitset<1001> bits1;
        bitset<1001> bits2;
        vector<int> ans;

        for(int num : nums1) bits1.set(num);
        for(int num : nums2) bits2.set(num);

        for(int i = 0; i <= 1000; i++){
            if(bits1[i] && bits2[i]){
                ans.push_back(i);
            }
        }

        return ans;
    }
};