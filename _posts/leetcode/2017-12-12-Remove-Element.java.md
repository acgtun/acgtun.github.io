---
layout: post
title: Remove Element
date: 2017-12-12 18:33:48
categories: leetcode
---

```java
public class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0;
        for(int i = 0;i < nums.length;++i) {
            if(nums[i] != val) {
                nums[k++] = nums[i];
            }
        }
        
        return k;
    }
}
```