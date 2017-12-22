---
layout: post
title: Single Number.py
date: 2017-12-12 18:37:13
categories: leetcode
---

```python
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        self = 0;
        for x in nums:
            self ^= x;
        return self;

```