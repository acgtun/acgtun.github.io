---
layout: post
title: Container With Most Water
date: 2017-12-12 18:33:48
categories: leetcode
---

```java
public class Solution {
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
```