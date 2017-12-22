---
layout: post
title: Search in Rotated Sorted Array II
date: 2017-12-12 18:33:48
categories: leetcode
---

```java
public class Solution {
    public boolean search(int[] nums, int target) {
        int n = nums.length;
        if(n == 0) {
            return false;
        }
        
        int l = 0, h = n - 1;
        while(l <= h) {
            int m = l + (h - l + 1) / 2;
            if(nums[m] == target) {
                return true;
            }
            
            if(nums[m] == nums[l]) {
                l = l + 1;
            } else if(nums[m] > nums[l]) {
                if(target >= nums[l] && target < nums[m]) {
                    h = m - 1;
                } else {
                    l = m + 1;
                }
            } else {
                if(target > nums[m] && target <= nums[h]) {
                    l = m + 1;
                } else {
                    h = m - 1;
                }
            }
        }
        return false;
    }
}
```