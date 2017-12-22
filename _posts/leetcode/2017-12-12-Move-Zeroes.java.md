---
layout: post
title: Move Zeroes
date: 2017-12-12 18:33:48
categories: leetcode
---

```java
public class Solution {
    public void moveZeroes(int[] nums) {
        int i = 0;
        int j = 0;
        while(i < nums.length) {
            if(nums[i] != 0) {
                nums[j] = nums[i];
                j++;
                i++;
            } else {
                i++;
            }
        }
        while(j < nums.length) {
            nums[j] = 0;
            j++;
        }
    }
}
```