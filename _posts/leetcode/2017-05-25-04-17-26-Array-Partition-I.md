---
layout: post
title: Array Partition I
date: 2017-05-25 04:17:26
categories: leetcode
---

```java
{{ % raw %}}
{{public class Solution {
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        int i = 0;
        int sum = 0;
        while(i < n) {
            sum += nums[i];
            i += 2;
        }
        return sum;
    }
}
}}
{{ % endraw %}}
```