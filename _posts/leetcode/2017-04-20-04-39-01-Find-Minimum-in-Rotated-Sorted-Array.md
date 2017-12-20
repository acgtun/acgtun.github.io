---
layout: post
title: Find Minimum in Rotated Sorted Array
date: 2017-04-20 04:39:01
categories: leetcode
---

```cpp
{{ % raw %}}
{{class Solution {
public:
    int findMin(vector<int>& nums) {
        if(nums.size() == 0) return 0;
        
        int ret = nums[0];
        int l = 0, h = nums.size() - 1;
        while(l <= h) {
            int m = (l + h) / 2;
            if(nums[m] >= nums[l]) {
                ret = min(ret, nums[l]);
                l = m + 1;
            } else {
                ret = min(ret, nums[m]);
                h = m - 1;
            }
        }
        
        return ret;
    }
};
}}
{{ % endraw %}}
```