---
layout: post
title: Reverse Linked List
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
    public ListNode reverseList(ListNode head) {
        if(head == null || head.next == null) return head;
        
        ListNode p = head;
        ListNode q = head.next;
        while(p != null && q != null) {
            ListNode t = q.next;
            
            q.next = p;
            
            p = q;
            q = t;
        }
        head.next = null;
        
        return p;
    }
}
}}
{{ % endraw %}}
```