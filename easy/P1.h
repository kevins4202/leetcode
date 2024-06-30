#include <iostream>
#include <vector>
using namespace std;

class P1 {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map <int, int> m;
        
        for(int i = 0; i < nums.size(); i++){
            int c = target - nums[i];

            if(m.count(c)){
                return {m[c], i};
            }

            m[nums[i]] = i;
        }
        return {};
    }
};