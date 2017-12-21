---
layout: post
title: Delete Node in a Linked List
date: 2017-12-21 02:16:04
categories: leetcode
---

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void deleteNode(ListNode node) {
        if(node == null) return ;
        if(node.next == null) return ;
        node.val = node.next.val;
        node.next = node.next.next;
    }
}
```