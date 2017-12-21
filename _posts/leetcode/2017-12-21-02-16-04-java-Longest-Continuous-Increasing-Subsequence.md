---
layout: post
title: Longest Continuous Increasing Subsequence
date: 2017-12-21 02:16:04
categories: leetcode
---

```java
class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int n = nums.length;
        if(n < 2) return n;
        
        int ret = 1;
        int cnt = 1;
        for(int i = 1;i < n;++i) {
            if(nums[i] > nums[i - 1]) cnt++;
            else {
                ret = Math.max(ret, cnt);
                cnt = 1;
            }
        }
        ret = Math.max(ret, cnt);
        return ret;        
    }
}
```