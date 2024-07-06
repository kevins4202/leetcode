

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
    int countNodes(TreeNode* root) {
        if(!root) return 0;

        int lh = hl(root), rh = hr(root);

        if(lh == rh) return (1<<lh) - 1;
        else return 1 + countNodes(root -> left) + countNodes(root -> right);
    }

    int hl(TreeNode* r){
        if(!r) return 0;
        return 1 + hl(r -> left);
    }

    int hr(TreeNode* r){
        if(!r) return 0;
        return 1 + hr(r -> right);
    }
};