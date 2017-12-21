---
layout: post
title: Two Sum II - Input array is sorted
date: 2017-12-21 02:16:04
categories: leetcode
---

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        if(numbers.size() < 2) {
            return vector<int>{};
        }
        int i = 0, j = numbers.size() - 1;
        while(i < j) {
            if(numbers[i] + numbers[j] == target) {
                return vector<int>{i + 1, j + 1};
            } else if(numbers[i] + numbers[j] > target) {
                j--;
            } else {
                i++;
            }
        }
    }
};
```