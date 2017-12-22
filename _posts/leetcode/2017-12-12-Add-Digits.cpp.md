---
layout: post
title: Add Digits
date: 2017-12-12 18:33:48
categories: leetcode
---

```cpp
class Solution {
public:
    int addDigits(int num) {
       
        return num - 9 * ((num - 1) / 9);
        
    }
};
```