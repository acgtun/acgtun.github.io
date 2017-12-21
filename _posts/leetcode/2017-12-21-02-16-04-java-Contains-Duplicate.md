---
layout: post
title: Contains Duplicate
date: 2017-12-21 02:16:04
categories: leetcode
---

```java
public class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for(int i = 0;i < nums.length;++i) {
            if(set.contains(nums[i])) {
                return true;
            }
            set.add(nums[i]);
        }
        
        return false;
    }
}
```