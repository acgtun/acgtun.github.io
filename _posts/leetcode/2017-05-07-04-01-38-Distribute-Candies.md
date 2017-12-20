---
layout: post
title: Distribute Candies
date: 2017-05-07 04:01:38
categories: leetcode
---

```java
{{ % raw %}}
{{public class Solution {
    public int distributeCandies(int[] candies) {
        int n = candies.length;
        if(n == 0) {
            return 0;
        }
        
        HashSet<Integer> set = new HashSet<>();
        for(int i = 0;i < n;++i) {
            set.add(candies[i]);
        }
        
        int m = n / 2;
        if(set.size() > m) {
            return m;
        } else {
            return set.size();
        }
    }
}
}}
{{ % endraw %}}
```