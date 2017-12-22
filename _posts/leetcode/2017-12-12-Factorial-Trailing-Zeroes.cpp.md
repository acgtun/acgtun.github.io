---
layout: post
title: Factorial Trailing Zeroes
date: 2017-12-12 18:33:48
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