---
layout: post
title: Best Time to Buy and Sell Stock
date: 2017-12-12 18:33:48
categories: leetcode
---

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ret = 0;
        size_t n = prices.size();
        if(n == 0 || n == 1) return ret;
        int minp = prices[0];
        for(size_t i = 1;i < n;++i) {
            ret = max(ret, prices[i] - minp);
            minp = min(minp, prices[i]);
        }
        
        return ret;
    }
};
```