---
layout: post
title: First Bad Version
date: 2017-12-21 02:16:04
categories: leetcode
---

```cpp
// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int l = 1, h = n;
        while(l < h) {
            int m = l + (h - l) / 2;
            if(isBadVersion(m)) {
                h = m;
            } else {
                l = m + 1;
            }
        }
        
        return l;
    }
};
```