---
layout: post
title: Best Time to Buy and Sell Stock
date: 2017-12-12 18:33:48
categories: leetcode
---

```java
public class Solution {
    public int maxProfit(int[] prices) {
        if(prices.length == 0) return 0;
        int minPrice = prices[0];
        int maxP = 0;
        for(int i = 1;i < prices.length;++i) {
            if(prices[i] > minPrice) {
                maxP = Math.max(maxP, prices[i] - minPrice);
            } else {
                minPrice = prices[i];
            }
        }
        
        return maxP;
    }
}
```