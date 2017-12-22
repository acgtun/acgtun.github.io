---
layout: post
title: Pascal's Triangle
date: 2017-12-12 18:33:48
categories: leetcode
---

```cpp
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int> > ret;
        if(numRows == 0) return ret;
        vector<int> row;
        row.push_back(1);
        ret.push_back(row);
        for(int i = 1;i <= numRows - 1;++i) {
            row.clear();
            row.push_back(1);
            for(int j = 1;j < i;++j) {
                row.push_back(ret[i - 1][j - 1] + ret[i - 1][j]);
            }
            row.push_back(1);
            ret.push_back(row);
        }
        
        return ret;
    }
};
```