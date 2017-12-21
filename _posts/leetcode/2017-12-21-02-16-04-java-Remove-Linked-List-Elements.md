---
layout: post
title: Remove Linked List Elements
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
    public ListNode removeElements(ListNode head, int val) {
        if(head == null) {
            return head;
        }
        
        if(head.val == val) {
            return removeElements(head.next, val);    
        }
        
        ListNode p = head;
        while(p.next != null) {
            if(p.next.val == val) {
                p.next = p.next.next;
            } else {
                p = p.next;
            }
        }
        
        return head;
    }
}
```