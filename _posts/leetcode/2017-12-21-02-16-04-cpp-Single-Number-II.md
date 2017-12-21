---
layout: post
title: Single Number II
date: 2017-12-21 02:16:04
categories: leetcode
---

```cpp
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        vector<int> one(32, 0);
        for(int i = 0;i < nums.size();++i) {
            int p = 1;
            for(int j = 0;j < 32;++j) {
                one[j] += ((nums[i] & p) != 0);
                p *= 2;
            }
        }
        for(int j = 0;j < 32;++j) {
            one[j] = one[j] % 3;
        }
        int ret = 0;
        int p = 1;
        for(int j = 0;j < 32;j++) {
            ret += (one[j] == 1 ? p : 0);
            p *= 2;
        }
        return ret;
    }
};
```