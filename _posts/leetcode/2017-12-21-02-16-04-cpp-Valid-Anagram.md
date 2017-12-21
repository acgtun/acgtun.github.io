---
layout: post
title: Valid Anagram
date: 2017-12-21 02:16:04
categories: leetcode
---

```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        if(s == t) return true;
        return false;
        
    }
};
```