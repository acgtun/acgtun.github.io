---
layout: post
title: Number of 1 Bits
date: 2017-12-12 18:33:48
categories: leetcode
---

```cpp
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int ret = 0;
        while(n) {
            n = n & (n -1);
            ret++;
        }
        
        return ret;
    }
};
```