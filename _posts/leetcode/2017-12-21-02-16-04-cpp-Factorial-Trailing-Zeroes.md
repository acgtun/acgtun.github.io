---
layout: post
title: Factorial Trailing Zeroes
date: 2017-12-21 02:16:04
categories: leetcode
---

```cpp
class Solution {
public:
    int trailingZeroes(int n) {
        int ret = 0;
        while(n) {
            ret += n / 5;
            n /= 5;
        }
        return ret;
    }
};
```