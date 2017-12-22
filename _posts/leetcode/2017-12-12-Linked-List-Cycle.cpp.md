---
layout: post
title: Linked List Cycle
date: 2017-12-12 18:33:48
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
    bool hasCycle(ListNode *head) {
        if(head == NULL) return false;
        
        ListNode* p = head;
        ListNode* q = head;
        while(p != NULL && p->next != NULL && q != NULL && q->next != NULL) {
            p = p->next;
            q = q->next->next;
            if(p == q) return true;
        }
        
        return false;
    }
};
```