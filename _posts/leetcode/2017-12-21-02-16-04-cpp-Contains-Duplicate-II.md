---
layout: post
title: Contains Duplicate II
date: 2017-12-21 02:16:04
categories: leetcode
---

```cpp
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        if(k <= 0) return false;
        
        unordered_set<int> hash_table;
        int j = 0;
        for(int i = 0;i < nums.size();++i) {
            if(hash_table.find(nums[i]) != hash_table.end()) return true;
            
            if(hash_table.size() == k) {
                hash_table.erase(nums[j]);
                j++;
            }
            hash_table.insert(nums[i]);
        }
        
        return false;
    }
};
```