---
layout: post
title: Minimum Depth of Binary Tree
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
    int minDepth(TreeNode* root) {
        if(root == NULL) return 0;
        
        if(root->left == NULL) return minDepth(root->right) + 1;
        else if(root->right == NULL) return minDepth(root->left) + 1;
        else return min(minDepth(root->left), minDepth(root->right)) + 1;
        
    }
};
```