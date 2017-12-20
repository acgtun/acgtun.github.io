---
layout: post
title: Binary Number with Alternating Bits
date: 2017-10-25 03:37:52
categories: leetcode
---

```java
{{ % raw %}}
{{class Solution {
    public boolean hasAlternatingBits(int n) {
        String s = Integer.toBinaryString(n);
        for(int i = 1;i < s.length();++i) {
            if(s.charAt(i) == s.charAt(i - 1))
                return false;
        }
        return true;
    }
}
}}
{{ % endraw %}}
```