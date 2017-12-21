---
layout: post
title: 4 Keys Keyboard
date: 2017-12-21 02:16:04
categories: leetcode
---

```java
public class Solution {
    public int maxA(int N) {
        int[] f = new int[Math.max(5, N + 1)];
        for(int i = 0;i <= N;++i) {
            f[i] = i;
        }
        
        for(int i = 5;i <= N;++i) {
            for(int j = 1;j < i;++j) {
                f[i] = Math.max(f[i], (i - j - 2) * f[j] + f[j]);   
            }
        }
        
        return f[N];
    }
}
```