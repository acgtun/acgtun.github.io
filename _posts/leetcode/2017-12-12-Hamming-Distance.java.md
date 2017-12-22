---
layout: post
title: Hamming Distance
date: 2017-12-12 18:33:48
categories: leetcode
---

```java
public class Solution {
    public int hammingDistance(int x, int y) {
        int z = x ^ y;
        int c = 0;
        while(z != 0) {
            z = z & (z - 1);
            c++;
        }
        return c;
    }
}
```