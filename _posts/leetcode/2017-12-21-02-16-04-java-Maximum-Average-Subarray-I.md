---
layout: post
title: Maximum Average Subarray I
date: 2017-12-21 02:16:04
categories: leetcode
---

```java

public class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double sum = 0.0;
        for(int i = 0;i < k;++i) {
            sum += nums[i];
        }
        double maxSum = sum;
        for(int i = k;i < nums.length;++i) {
            sum -= nums[i - k];
            sum += nums[i];
            maxSum = Math.max(sum, maxSum);
        }
        
        return maxSum / k;
    }
}
```