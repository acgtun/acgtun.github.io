---
layout: post
title: Remove Duplicates from Sorted List
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
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null || head.next == null) return head;
        
        ListNode p = head;
        while(p.next != null) {
            if(p.next.val == p.val) {
                p.next = p.next.next;
            } else {
                p = p.next;
            }
        }
        
        return head;
    }
}
}}
{{ % endraw %}}
```