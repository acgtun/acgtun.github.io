---
layout: post
title: Reverse Bits
date: 2017-12-12 18:33:48
categories: leetcode
---

```java
public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int res = 0;
        for(int i = 0;i < 32;++i) {
            res <<= 1;
            int bit = 1 << i;
            res += (n & bit) >>> i;
        }
        
        return res;
    }
}
```