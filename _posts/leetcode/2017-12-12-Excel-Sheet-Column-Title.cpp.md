---
layout: post
title: Excel Sheet Column Title
date: 2017-12-12 18:33:48
categories: leetcode
---

```cpp
class Solution {
public:
    string convertToTitle(int n) {
        string ret;
        while(n > 0) {
            ret += (n - 1) % 26 + 'A';
            n = (n - 1) / 26;
        }
        reverse(ret.begin(), ret.end());
        return ret;
    }
};
```