---
layout: post
title: Excel Sheet Column Title
date: 2017-12-21 02:16:04
categories: leetcode
---

```java
public class Solution {
    public String convertToTitle(int n) {
        StringBuilder res = new StringBuilder();
        while(n != 0) {
            res.append((char)((n - 1) % 26 + 'A'));
            n = (n - 1) / 26;
        }
        
        return res.reverse().toString();
    }
}
```