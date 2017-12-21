---
layout: post
title: Pascal's Triangle II
date: 2017-12-21 02:16:04
categories: leetcode
---

```cpp
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        if(rowIndex == 0) {
            vector<int> ret(1, 1);
            return ret;
        }
        vector<int> pre;
        pre.push_back(1);
        pre.push_back(1);
        vector<int> cur;
        for(int i = 2;i <= rowIndex;++i) {
            cur.clear();
            cur.resize(i + 1, 0);
            cur[0] = 1;
            for(int j = 1;j < i;j++) {
                cur[j] = pre[j] + pre[j - 1];
            }
            cur[i] = 1;
            pre = cur;
        }
        
        return pre;
    }
};
```