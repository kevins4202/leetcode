#include "../stdc++.h"
using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int total = nums.size() * (nums.size() + 1) / 2;

        for(int x : nums) total -= x;

        return total;
    }
};