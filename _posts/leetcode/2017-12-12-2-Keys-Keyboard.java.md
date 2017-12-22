---
layout: post
title: 2 Keys Keyboard
date: 2017-12-12 18:33:48
categories: leetcode
---

```java
public class Solution {
    public int minSteps(int n) {
        int[] f = new int[Math.max(5, n + 1)];
        f[1] = 0;
        f[2] = 2;
        f[3] = 3;
        for(int i = 4;i <= n;++i) {
            f[i] = i;
            for(int j = 2;j < n;++j) {
                if(i % j == 0) {
                    f[i] = Math.min(f[i], f[j] + i / j);
                }
            }
        }
        return f[n];
    }
}
```