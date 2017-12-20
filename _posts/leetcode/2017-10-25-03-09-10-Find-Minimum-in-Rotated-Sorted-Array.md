---
layout: post
title: Find Minimum in Rotated Sorted Array
date: 2017-10-25 03:09:10
categories: leetcode
---

```java
{{ % raw %}}
{{class Solution {
    public int findMin(int[] nums) {
        int n = nums.length;
        if(n == 0) throw new IllegalArgumentException();
        
        int minNum = nums[0];
        int low = 0, high = n - 1;
        while(low < high) {
            int mid = low + (high - low) / 2;
            if(nums[mid] >= nums[low]) {
                minNum = Math.min(minNum, nums[low]);
                low = mid + 1;
            } else {
                minNum = Math.min(minNum, nums[mid]);
                high = mid - 1;
            }
        }
        
        minNum = Math.min(minNum, nums[low]);
        return minNum;
    }
}
}}
{{ % endraw %}}
```