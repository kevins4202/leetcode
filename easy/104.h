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
    int maxDepth(TreeNode* root) {
        if(!root) return 0;
        return depth(root, 0);
    }

    int depth(TreeNode* root, int dep){
        if(!root) return dep;

        return max(depth(root-> left, dep + 1), depth(root -> right, dep + 1));
    }
};