---
layout: post
title: Populating Next Right Pointers in Each Node II
date: 2017-08-14 01:05:35
categories: leetcode
---

```java
{{ % raw %}}
{{/**
 * Definition for binary tree with next pointer.
 * public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */
public class Solution {
    private TreeLinkNode getNext(TreeLinkNode root) {
        TreeLinkNode p = root;
        while(p.next != null) {
            p = p.next;
            if(p.left != null) return p.left;
            if(p.right != null) return p.right;
        }
        return null;
    }
    
    public void connect(TreeLinkNode root) {
        if(root == null) return ;

        if(root.left == null && root.right == null) return ;
        if(root.left != null && root.right != null) {
            root.left.next = root.right;
            root.right.next = getNext(root);
        } else if(root.left == null && root.right != null) {
            root.right.next = getNext(root);
        } else {
            root.left.next = getNext(root);
        }
       
        connect(root.right); // right first
        connect(root.left);
    }
}
}}
{{ % endraw %}}
```