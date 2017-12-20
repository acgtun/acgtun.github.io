---
layout: post
title: Min Cost Climbing Stairs
date: 2017-12-17 20:06:55
categories: leetcode
---

```java
{{ % raw %}}
{{class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        int[] opt = new int[n];
        opt[0] = cost[0];
        opt[1] = cost[1];
        for(int i = 2;i < n;++i) {
            opt[i] = Math.min(opt[i - 1], opt[i - 2]) + cost[i];
        }
        return Math.min(opt[n - 1], opt[n - 2]);
    }
}
}}
{{ % endraw %}}
```