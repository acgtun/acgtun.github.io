---
layout: post
title: Maximum Product of Three Numbers
date: 2017-07-07 01:32:55
categories: leetcode
---

```java
{{ % raw %}}
{{public class Solution {
    public int maximumProduct(int[] nums) {
        int n = nums.length;
        if(n < 3) {
            throw new IllegalArgumentException();
        }
        Arrays.sort(nums);
        return Math.max(nums[n - 1] * nums[n - 2] * nums[n - 3], nums[n - 1] * nums[0] * nums[1]);
    }
}
}}
{{ % endraw %}}
```