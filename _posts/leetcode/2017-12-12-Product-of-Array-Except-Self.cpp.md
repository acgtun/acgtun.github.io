---
layout: post
title: Product of Array Except Self
date: 2017-12-12 18:33:48
categories: leetcode
---

```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> ret(n, 1);
        for(int i = 1;i < n;++i) {
            ret[i] = ret[i - 1] * nums[i - 1];
        }
        
        int r = 1;
        for(int i = n - 1;i >= 0;--i) {
            ret[i] = r * ret[i];
            r *= nums[i];
        }
        
        return ret;
    }
};
```