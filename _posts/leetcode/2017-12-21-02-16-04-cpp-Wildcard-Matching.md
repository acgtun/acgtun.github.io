---
layout: post
title: Wildcard Matching
date: 2017-12-21 02:16:04
categories: leetcode
---

```cpp
class Solution {
 public:
  bool isMatch(string s, string p) {
    int m = s.size(), n = p.size();
    int i = 0, j = 0;
    int pstar = -1, pstari = -1;

    while (i < m) {
      if (j < n && (p[j] == '?' || p[j] == s[i])) {
        i++;
        j++;
      } else if (j < n && p[j] == '*') {
        pstar = j;
        pstari = i;
        j++;
      } else if (pstari != -1) {
        j = pstar + 1;
        i = pstari++;
      } else {
        return false;
      }
    }

    while (j < n) {
      if (p[j] == '*') {
        j++;
      } else {
        return false;
      }
    }

    return true;
  }
};

```