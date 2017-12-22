---
layout: post
title: Search in Rotated Sorted Array
date: 2017-12-12 18:33:48
categories: leetcode
---

```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        int l = 0, r = n - 1;
        while(l <= r) {
            int m = l + (r - l) / 2;
            
            if(nums[m] == target) {
                return m;
            }
            
            if(nums[m] >= nums[l]) { // l ~ m increasing
                if(target >= nums[l] && target < nums[m]) r = m - 1;
                else l = m + 1;
            } else if(nums[m] < nums[l]) { //m to r increasing
                if(target > nums[m] && target <= nums[r]) l = m + 1;
                else r = m - 1;
            }
        }
        
        return -1;
    }
};
```