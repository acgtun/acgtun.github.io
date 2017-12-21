---
layout: post
title: Excel Sheet Column Number
date: 2017-12-21 02:16:04
categories: leetcode
---

```cpp
class Solution {
public:
    int titleToNumber(string s) {
        int num = 0;
        for(size_t i = 0;i < s.size();++i) {
            num = num * 26 + (s[i] - 'A') + 1;
        }
        
        return num;
    }
};
```