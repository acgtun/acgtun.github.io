---
layout: post
title: Invert Binary Tree
date: 2017-04-20 04:39:01
categories: leetcode
---

```cpp
{{ % raw %}}
{{/**
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
}}
{{ % endraw %}}
```