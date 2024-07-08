#include "../stdc++.h"
using namespace std;
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> v1(1001, 0);
        vector<int> v2(1001, 0);
        vector<int> ans;

        for(int num : nums1) v1[num]++;
        for(int num : nums2) v2[num]++;

        for(int i = 0; i <= 1000; i++){
            int x = min(v1[i], v2[i]);

            for(int j = 0; j < x; j++) ans.push_back(i);
        }

        return ans;
    }
};