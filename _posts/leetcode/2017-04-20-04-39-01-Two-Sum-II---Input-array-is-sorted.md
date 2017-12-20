---
layout: post
title: Two Sum II - Input array is sorted
date: 2017-04-20 04:39:01
categories: leetcode
---

```java
{{ % raw %}}
{{public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i = 0, j = numbers.length - 1;
        while(i < j) {
            int s = numbers[i] + numbers[j];
            if(s > target) j--;
            else if(s < target) i++;
            else {
                return new int[]{i + 1, j + 1};
            }
        }
        
        throw new IllegalArgumentException("No Solution");
    }
}
}}
{{ % endraw %}}
```