---
layout: post
title: Binary Tree Longest Consecutive Sequence
date: 2017-05-25 02:59:53
categories: leetcode
---

```java
{{ % raw %}}
{{/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    int ret = 0;
    
    private void helper(TreeNode root, int r) {
        ret = Math.max(ret, r);
        if(root.left != null) {
            if(root.left.val == root.val + 1) {
                helper(root.left, r + 1);
            } else {
                helper(root.left, 1);
            }
        }
        if(root.right != null) {
            if(root.right.val == root.val + 1) {
                helper(root.right, r + 1);
            } else {
                helper(root.right, 1);
            }
        }
    }
    
    public int longestConsecutive(TreeNode root) {
        if(root == null) {
            return 0;
        }
        
        helper(root, 1);
        return ret;
    }
}
}}
{{ % endraw %}}
```