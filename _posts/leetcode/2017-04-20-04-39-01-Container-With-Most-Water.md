---
layout: post
title: Container With Most Water
date: 2017-04-20 04:39:01
categories: leetcode
---

```java
{{ % raw %}}
{{public class Solution {
    public int maxArea(int[] height) {
        int res = 0;
        int i = 0, j = height.length - 1;
        while(i < j) {
            res = Math.max(res, Math.min(height[i], height[j]) * (j - i));
            if(height[i] < height[j]) i++;
            else j--;
        }
        
        return res;
    }
}
}}
{{ % endraw %}}
```