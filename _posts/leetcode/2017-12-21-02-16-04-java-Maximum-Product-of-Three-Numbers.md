---
layout: post
title: Maximum Product of Three Numbers
date: 2017-12-21 02:16:04
categories: leetcode
---

```java
public class Solution {
    public int maximumProduct(int[] nums) {
        int n = nums.length;
        if(n < 3) {
            throw new IllegalArgumentException();
        }
        Arrays.sort(nums);
        return Math.max(nums[n - 1] * nums[n - 2] * nums[n - 3], nums[n - 1] * nums[0] * nums[1]);
    }
}
```