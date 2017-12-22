---
layout: post
title: Power of Two
date: 2017-12-12 18:33:48
categories: leetcode
---

```cpp
class Solution {
public:
    bool isPowerOfTwo(int n) {
        if(n < 0) return false;
        if(n == 0) return false;
        return !(n & (n - 1));
    }
};
```