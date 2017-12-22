---
layout: post
title: Reverse Integer
date: 2017-12-12 18:33:48
categories: leetcode
---

```java
public class Solution {
    public int reverse(int x) {
        long y = x;
        y = Math.abs(y);
        
        long s = 0;
        while(y != 0) {
            s = s * 10 + y % 10;
            y = y / 10;
        }
        
        s = s * Integer.signum(x);
        
        if(s > Integer.MAX_VALUE) return 0;
        if(s < Integer.MIN_VALUE) return 0;
        
        return (int) s;
    }
}
```