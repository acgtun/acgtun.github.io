---
layout: post
title: Invert Binary Tree
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
    TreeNode* invertTree(TreeNode* root) {
        if(root == NULL) return root;
        invertTree(root->left);
        invertTree(root->right);
        
        swap(root->left, root->right);
        return root;
    }
};
```