---
layout: post
title: Binary Tree Preorder Traversal
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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ret;
        if(root == NULL) return ret;
        stack<TreeNode*> s;
        s.push(root);
        while(!s.empty()) {
            TreeNode* top = s.top();
            s.pop();
            
            ret.push_back(top->val);
            if(top->right) s.push(top->right);
            if(top->left) s.push(top->left);
            
        }
        
        return ret;
    }
};
```