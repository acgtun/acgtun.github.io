---
layout: post
title: Sum of Square Numbers
date: 2017-12-21 02:16:04
categories: leetcode
---

```java
public class Solution {
    public boolean judgeSquareSum(int c) {
        int n = (int) Math.sqrt(c);
        for(int a = 0;a <= n;++a) {
            int bSquare = c - a * a;
            long b = Math.round(Math.sqrt(bSquare));
            if(b * b == bSquare) {
                return true;
            }
        }
        return false;        
    }
}
```