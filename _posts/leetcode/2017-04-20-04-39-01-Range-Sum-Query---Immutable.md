---
layout: post
title: Range Sum Query - Immutable
date: 2017-04-20 04:39:01
categories: leetcode
---

```cpp
{{ % raw %}}
{{class NumArray {
public:
    vector<int> sum;
    NumArray(vector<int> &nums) {
        if(nums.size() == 0) return ;
        sum.resize(nums.size(), 0);
        sum[0] = nums[0];
        for(size_t i = 1;i < nums.size();++i) {
            sum[i] = sum[i - 1] + nums[i];
        }
    }

    int sumRange(int i, int j) {
       
        if(i == 0) return sum[j];
        return sum[j] - sum[i - 1];
    }
};


// Your NumArray object will be instantiated and called as such:
// NumArray numArray(nums);
// numArray.sumRange(0, 1);
// numArray.sumRange(1, 2);
}}
{{ % endraw %}}
```