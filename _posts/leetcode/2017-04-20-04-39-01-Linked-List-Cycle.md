---
layout: post
title: Linked List Cycle
date: 2017-04-20 04:39:01
categories: leetcode
---

```java
{{ % raw %}}
{{/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        if(head == null || head.next == null) return false;
        
        ListNode p = head;
        ListNode q = head.next;
        while(p != null && q != null && q.next != null) {
            if(p == q) return true;
            p = p.next;
            q = q.next.next;
        }
        
        return false;
    }
}
}}
{{ % endraw %}}
```