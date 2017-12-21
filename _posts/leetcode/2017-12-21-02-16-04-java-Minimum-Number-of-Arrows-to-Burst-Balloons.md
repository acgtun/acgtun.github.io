---
layout: post
title: Minimum Number of Arrows to Burst Balloons
date: 2017-12-21 02:16:04
categories: leetcode
---

```java
class Solution {
    public int findMinArrowShots(int[][] points) {
        if(points.length == 0) return 0;
        
        Arrays.sort(points, (a, b) -> a[1] - b[1]);
        int count = 1, end = points[0][1];
        for(int i = 1;i < points.length;++i) {
            if(points[i][0] > end) {
                count++;
                end = points[i][1];
            }
        }
        return count;
    }
}
```