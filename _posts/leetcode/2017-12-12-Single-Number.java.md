---
layout: post
title: Single Number
date: 2017-12-12 18:33:48
categories: leetcode
---

```java
public class Solution {
    public int singleNumber(int[] nums) {
        int res = 0;
        for(int i = 0;i < nums.length;++i) {
            res ^= nums[i];
        }
        
        return res;
    }
}
```