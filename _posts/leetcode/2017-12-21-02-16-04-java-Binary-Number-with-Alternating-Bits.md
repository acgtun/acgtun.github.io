---
layout: post
title: Binary Number with Alternating Bits
date: 2017-12-21 02:16:04
categories: leetcode
---

```java
class Solution {
    public boolean hasAlternatingBits(int n) {
        String s = Integer.toBinaryString(n);
        for(int i = 1;i < s.length();++i) {
            if(s.charAt(i) == s.charAt(i - 1))
                return false;
        }
        return true;
    }
}
```