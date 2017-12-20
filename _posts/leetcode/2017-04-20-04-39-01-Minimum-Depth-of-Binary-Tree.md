---
layout: post
title: Minimum Depth of Binary Tree
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
    int minDepth(TreeNode* root) {
        if(root == NULL) return 0;
        
        if(root->left == NULL) return minDepth(root->right) + 1;
        else if(root->right == NULL) return minDepth(root->left) + 1;
        else return min(minDepth(root->left), minDepth(root->right)) + 1;
        
    }
};
}}
{{ % endraw %}}
```