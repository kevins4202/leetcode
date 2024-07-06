#include "../stdc++.h"
using namespace std;

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(!root) return root;

        auto tmp = root-> right;
        root -> right = root -> left;
        root -> left = tmp;

        invertTree(root -> left);
        invertTree(root -> right);

        return root;
    }

    
};