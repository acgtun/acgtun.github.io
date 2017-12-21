---
layout: post
title: Reverse String
date: 2017-12-21 02:16:04
categories: leetcode
---

```java
public class Solution {
    public String reverseString(String s) {
        StringBuffer res = new StringBuffer(s);
        int n = res.length();
        for(int i = 0;i < n / 2;i++) {
            char t = res.charAt(i);
            res.setCharAt(i, res.charAt(n - 1 - i));
            res.setCharAt(n - 1 - i, t);
        }
        
        return res.toString();
    }
}
```