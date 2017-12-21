---
layout: post
title: Implement strStr()
date: 2017-12-21 02:16:04
categories: leetcode
---

```cpp
class Solution {
public:
    int strStr(string haystack, string needle) {
        size_t p = haystack.find(needle);
        if(p == string::npos) return -1;
        
        return p;
    }
};
```