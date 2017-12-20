---
layout: post
title: 1-bit and 2-bit Characters
date: 2017-10-29 03:54:16
categories: leetcode
---

```java
{{ % raw %}}
{{class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        int n = bits.length;
        if(n == 1) return true;
    
        int index = 0;
        while(index < n) {
            if(index == n - 1) return true;
            if(bits[index] == 0) index++;
            else index += 2;
        }
        return false;        
    }
}
}}
{{ % endraw %}}
```