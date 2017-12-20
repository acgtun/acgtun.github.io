---
layout: post
title: Hamming Distance
date: 2017-07-22 16:52:54
categories: leetcode
---

```java
{{ % raw %}}
{{public class Solution {
    public int hammingDistance(int x, int y) {
        int z = x ^ y;
        int c = 0;
        while(z != 0) {
            z = z & (z - 1);
            c++;
        }
        return c;
    }
}
}}
{{ % endraw %}}
```