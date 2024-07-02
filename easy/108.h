#include "../stdc++.h"
using namespace std;


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        // TreeNode* root;
        // root = build(0, nums.size() - 1, nums);
        return build(0, nums.size() - 1, nums);
        // return root;
    }

    TreeNode* build(int lo, int hi, vector<int> nums){
        if(lo > hi) return nullptr;
        int mid = lo + (hi - lo)/2;
        TreeNode* tmp = new TreeNode(nums[mid]);
        cout<<nums[mid]<<endl;

        tmp -> left = build(lo, mid-1, nums);
        tmp -> right = build(mid+1, hi, nums);

        return tmp;
    }
};