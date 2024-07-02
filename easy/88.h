#include "../stdc++.h"
using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = m - 1;
        int j = n - 1;

        int k = m + n - 1;
        for(; k >= 0; k--){
            if(i < 0 || j < 0) break;
            if(nums1[i] > nums2[j]){
                nums1[k] = nums1[i];
                i--;
            } else{
                nums1[k] = nums2[j];
                j--;
            }
        }

        while(j >= 0) {
            nums1[k] = nums2[j];
            j--;
            k--;
        }

        while(i >= 0) {
            nums1[k] = nums1[i];
            i--;
            k--;
        }

        
    }
};