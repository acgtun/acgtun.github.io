---
layout: post
title: Merge Two Binary Trees
date: 2017-06-12 03:02:55
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
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        if(t1 == null && t2 == null) {
            return null;
        }
        if(t1 == null && t2 != null) {
            return t2;
        }
        if(t1 != null && t2 == null) {
            return t1;
        }
        
        TreeNode mergeNode = new TreeNode(t1.val + t2.val);
        mergeNode.left = mergeTrees(t1.left, t2.left);
        mergeNode.right = mergeTrees(t1.right, t2.right);
        
        return mergeNode;
    }
}
}}
{{ % endraw %}}
```