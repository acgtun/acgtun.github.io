---
layout: post
title: Binary Tree Postorder Traversal
date: 2017-12-21 02:16:04
categories: leetcode
---

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ret;
        if(root == NULL) return ret;

        stack<TreeNode*> s;
        TreeNode* p = root;
        while(p != NULL) {
            if(p->right != NULL) {
                s.push(p->right);
            }
            s.push(p);
            p = p->left;
        }
        
        while(!s.empty()) {
            TreeNode* cur = s.top();
            s.pop();
            
            if(cur->right != NULL && s.empty() == false && s.top() == cur->right) {
                TreeNode* right = s.top();
                s.pop();
                s.push(cur);
                
                TreeNode* p = right;
                while(p != NULL) {
                    if(p->right != NULL) {
                        s.push(p->right);
                    }
                    s.push(p);
                    p = p->left;
                }
            } else {
                ret.push_back(cur->val);
            }
        }
        
        return ret;
    }
};
```