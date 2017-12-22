---
layout: post
title: Remove Duplicates from Sorted Array
date: 2017-12-12 18:33:48
categories: leetcode
---

```cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size() == 0) return 0;
        int j = 1;
        for(int i = 1;i < nums.size();++i) {
            if(nums[i] == nums[j - 1]) continue; 
            else {
                nums[j] = nums[i];
                j++;
            }
        }
        
        return j;
    }
};
```