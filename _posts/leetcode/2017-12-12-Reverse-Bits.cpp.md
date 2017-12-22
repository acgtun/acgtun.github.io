---
layout: post
title: Reverse Bits
date: 2017-12-12 18:33:48
categories: leetcode
---

```cpp
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t ret = 0;
        for(int i = 0;i < 32;++i) {
            ret <<= 1;
            ret += n & 0x1;
            n >>= 1;
        }
        return ret;
    }
};
```