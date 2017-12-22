---
layout: post
title: Symmetric Tree
date: 2017-12-12 18:33:48
categories: leetcode
---

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    private boolean isSymmetric(TreeNode left, TreeNode right) {
        if(left == null && right == null) {
            return true;
        }
        
        if(left == null || right == null) {
            return false;
        }
        
        if(left.val != right.val) {
            return false;
        }
        
        return isSymmetric(left.left, right.right) && isSymmetric(left.right, right.left);
    }
    
    public boolean isSymmetric(TreeNode root) {
        if(root == null) return true;
        return isSymmetric(root.left, root.right);
    }
}
```