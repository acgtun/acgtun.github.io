---
layout: post
title: Palindrome Number
date: 2017-04-20 04:39:01
categories: leetcode
---

```java
{{ % raw %}}
{{public class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0) return false;
        
        int y = x;
        int s = 0;
        while(y != 0) {
            s = s * 10 + y % 10;
            y = y / 10;
        }
        
        if(s == x) return true;
        return false;
    }
}
}}
{{ % endraw %}}
```