---
layout: post
title: Ugly Number.py
date: 2017-12-12 18:37:18
categories: leetcode
---

```python
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        if num == 0:
            return False

        while num % 2 == 0:
            num //= 2
        while num % 3 == 0:
            num //= 3
        while num % 5 == 0:
            num //= 5

        if num == 1 or num == 0:
            return True
        return False

```