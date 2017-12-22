---
layout: post
title: First Bad Version.c
date: 2017-12-12 18:33:48
categories: leetcode
---

```cpp
// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

int firstBadVersion(int n) {
    uint32_t l = 1, h = n, m = 0;
    while(l < h) {
        m = (l + h) / 2;
        if(isBadVersion(m)) h = m;
        else l = m + 1;
    }
    return (int)l;
}
```