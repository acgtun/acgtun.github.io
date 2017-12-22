---
layout: post
title: Contains Duplicate II
date: 2017-12-12 18:33:48
categories: leetcode
---

```java
public class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        if(k <= 0) return false;
        HashSet<Integer> set = new HashSet<>();
        for(int i = 0;i < nums.length;++i) {
            if(i > k) {
                set.remove(nums[i - k- 1]);
            }
            
            if(set.contains(nums[i])) {
                return true;
            }
                
            set.add(nums[i]);
        }
        return false;
    }
}
```