---
layout: post
title: Maximum Distance in Arrays
date: 2017-12-12 18:33:48
categories: leetcode
---

```java
public class Solution {
    public int maxDistance(List<List<Integer>> arrays) {
        List<List<Integer> > copyArrays = new ArrayList<>();
        for(int i = 0;i < arrays.size();++i) {
            if(arrays.get(i).size() != 0) {
                copyArrays.add(arrays.get(i));
            }
        }
        copyArrays.sort((a, b) -> a.get(0) - b.get(0));
        int ret = 0;
        for(int i = 1;i < copyArrays.size();++i) {
            ret = Math.max(ret, Math.abs(copyArrays.get(i).get(copyArrays.get(i).size() - 1) - copyArrays.get(0).get(0)));
        }
        for(int i = 1;i < copyArrays.size();++i) {
            ret = Math.max(ret, Math.abs(copyArrays.get(i).get(0) - copyArrays.get(0).get(copyArrays.get(0).size() - 1)));
        }

        return ret;
    }
}
```