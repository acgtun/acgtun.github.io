---
layout: post
title: Coin Change 2
date: 2017-12-12 18:33:48
categories: leetcode
---

```java
public class Solution {
    public int change(int amount, int[] coins) {
        int[] opt = new int[amount + 1];
        Arrays.fill(opt, 0);
        opt[0] = 1;
        // avoid duplicates, add coins to build amount (everytime add different coins)
        // rather than build amount using coins
        for(int j = 0;j < coins.length;++j) {
            for(int i = 0;i <= amount;++i) {
                if(i - coins[j] >= 0) {
                    opt[i] += opt[i - coins[j]];
                }
            }
        }
        
        return opt[amount];        
    }
}
```