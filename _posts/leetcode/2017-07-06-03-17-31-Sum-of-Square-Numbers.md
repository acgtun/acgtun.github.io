---
layout: post
title: Sum of Square Numbers
date: 2017-07-06 03:17:31
categories: leetcode
---

```java
{{ % raw %}}
{{public class Solution {
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
}}
{{ % endraw %}}
```