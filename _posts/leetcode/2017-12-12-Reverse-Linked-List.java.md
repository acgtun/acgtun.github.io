---
layout: post
title: Reverse Linked List
date: 2017-12-12 18:33:48
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
```