---
layout: post
title: Number of 1 Bits
date: 2017-12-12 18:33:48
categories: leetcode
---

```java
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int res = 0;
        for(int i = 0;i < 32;++i) {
            int bit = 1 << i;
            res += (bit & n) >>> i;
        }
        
        return res;
    }
}
```