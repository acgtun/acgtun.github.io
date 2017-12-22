---
layout: post
title: Rotate Array
date: 2017-12-12 18:33:48
categories: leetcode
---

```cpp
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k = k % n;
        if(n == 0 || n == 1 || k == 0) return ;
        
        reverse(nums.begin(), nums.end());
        reverse(nums.begin(), nums.begin() + k);
        reverse(nums.begin() + k, nums.end());
    }
};
```