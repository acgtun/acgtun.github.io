---
layout: post
title: Remove Element
date: 2017-12-21 02:16:04
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