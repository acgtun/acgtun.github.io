---
layout: post
title: Search a 2D Matrix
date: 2017-12-12 18:33:48
categories: leetcode
---

```cpp
class Solution {
public:
    bool searchMatrix(vector<vector<int> >& matrix, int target) {
        int m = matrix.size();
        if(m == 0) return false;
        int n = matrix[0].size();
        if(n == 0) return false;
        
        int l = 0, r = m * n - 1;
        while(l <= r) {
            int mid = l + (r - l) / 2;
            
            int row = mid / n;
            int col = mid % n;
            
            if(matrix[row][col] == target) {
                return true;
            }
            
            if(matrix[row][col] > target) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        
        return false;
    }
};
```