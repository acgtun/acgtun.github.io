---
layout: post
title: Wiggle Sort
date: 2017-12-12 18:33:48
categories: leetcode
---

```cpp
class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        int sign = 1;
        for(int i = 1;i < nums.size();++i) {
            if((sign == 1 && nums[i] < nums[i - 1]) || (sign == -1 && nums[i] > nums[i - 1])) {
                swap(nums[i], nums[i - 1]);
            }
            sign *= -1;
        }
    }
};
```