---
layout: post
title: First Unique Character in a String
date: 2017-04-20 04:39:01
categories: leetcode
---

```java
{{ % raw %}}
{{public class Solution {
    public int firstUniqChar(String s) {
        int[] count = new int[26];
        Arrays.fill(count, 0);
        for(int i = 0;i < s.length();++i) {
            count[(int)(s.charAt(i) - 'a')]++;
        }
        
        for(int i = 0;i < s.length();++i) {
            if(count[(int)(s.charAt(i) - 'a')] == 1) return i;
        }
        
        return -1;
    }
}
}}
{{ % endraw %}}
```