---
layout: post
title: Missing Number
date: 2017-12-12 18:33:48
categories: leetcode
---

```cpp
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        nums.push_back(-1);
        for(int i = 0;i < nums.size();++i) {
            while(nums[i] != i && nums[i] != -1) {
                swap(nums[i], nums[nums[i]]);
            }
        }
        
        for(int i = 0;i < nums.size();++i) {
            if(nums[i] != i) return i;
        }
    }
};
```