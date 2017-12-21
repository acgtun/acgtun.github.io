---
layout: post
title: Merge Two Sorted Lists
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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* head = new ListNode(-1);
        
        ListNode* p = head;
        
        while(l1 != NULL && l2 != NULL) {
            if(l1->val <= l2->val) {
                p->next = l1;
                l1 = l1->next;
                p = p->next;
            } else {
                p->next = l2;
                l2 = l2->next;
                p = p->next;
            }
        }
        
        while(l1 != NULL) {
            p->next = l1;
            l1 = l1->next;
            p = p->next;
        }
        
        while(l2 != NULL) {
            p->next = l2;
            l2 = l2->next;
            p = p->next;
        }
        
        p = head->next;
        delete head;
        
        return p;
    }
};
```