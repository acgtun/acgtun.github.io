---
layout: post
title: Lowest Common Ancestor of a Binary Tree
date: 2017-12-12 18:33:48
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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root == NULL) return NULL;
        if(root == p || q == root) return root;
        
        TreeNode* l = lowestCommonAncestor(root->left, p, q);
        TreeNode* r = lowestCommonAncestor(root->right, p, q);
        
        if(l != NULL && r != NULL) return root;
        
        if(l != NULL) return l;
        if(r != NULL) return r;
        
    }
};
```