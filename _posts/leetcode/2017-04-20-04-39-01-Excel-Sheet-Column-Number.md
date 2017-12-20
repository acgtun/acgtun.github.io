---
layout: post
title: Excel Sheet Column Number
date: 2017-04-20 04:39:01
categories: leetcode
---

```java
{{ % raw %}}
{{public class Solution {
    public int titleToNumber(String s) {
        String rev = new StringBuilder(s).reverse().toString();
        int res = 0;
        int b = 1;
        for(int i = 0;i < rev.length();++i) {
            res += (rev.charAt(i) - 'A' + 1) * b;
            b *= 26;
        }
        
        return res;
    }
}
}}
{{ % endraw %}}
```