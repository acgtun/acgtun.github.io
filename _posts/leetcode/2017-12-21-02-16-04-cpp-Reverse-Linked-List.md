---
layout: post
title: Reverse Linked List
date: 2017-12-21 02:16:04
categories: leetcode
---

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(head == NULL || head->next == NULL) {
            return head;
        }
        
        ListNode *p = head, *q = head->next;
        while(p != NULL && q != NULL) {
            ListNode *t = q->next;
            q->next = p;
            
            // next
            p = q;
            q = t;
        }
        
        head->next = NULL;
        
        return p;
    }
};
```