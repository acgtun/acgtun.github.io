---
layout: post
title: Delete Node in a Linked List
date: 2017-04-20 04:39:01
categories: leetcode
---

```java
{{ % raw %}}
{{/**
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
}}
{{ % endraw %}}
```