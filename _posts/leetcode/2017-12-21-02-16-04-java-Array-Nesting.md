---
layout: post
title: Array Nesting
date: 2017-12-21 02:16:04
categories: leetcode
---

```java
public class Solution {
    public int arrayNesting(int[] nums) {
        int n = nums.length;
        if(n == 0) {
            return 0;
        }
        
        int[] root = new int[n];
        Arrays.fill(root, -1);
        int maxLen = -1;
        for(int i = 0;i < n;++i) {
            if(root[i] != -1) {
                continue;
            }
            int len = 1;
            root[i] = i;
            int j = nums[i];
            while(root[j] != i) {
                root[j] = i;
                j = nums[j];
                len++;
            }
            maxLen = Math.max(len, maxLen);
        }

        return maxLen;
    }
}
```