#include "../stdc++.h"
using namespace std;

struct Node{
    TreeNode* node;
    string path;
};
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> ans;

        queue<Node> q;
        q.push((Node) {root, to_string(root -> val)});

        while(!q.empty()){
            auto nd = q.front();
            q.pop();

            auto curr = nd.node;
            if(!curr -> left && !curr -> right){
                ans.push_back(nd.path);
            } else{
                if(curr -> left){
                    q.push((Node){curr -> left, nd.path + "->"+to_string(curr->left->val)});
                }

                if(curr -> right){
                    q.push((Node){curr -> right, nd.path + "->"+to_string(curr->right->val)});
                }
            }
        }

        return ans;
    }
};