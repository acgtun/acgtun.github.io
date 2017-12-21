---
layout: post
title: Judge Route Circle
date: 2017-12-21 02:16:04
categories: leetcode
---

```java
public class Solution {
    public boolean judgeCircle(String moves) {
        Map<Character, Integer> map = new HashMap<>();
        for(char c: moves.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        int u = map.getOrDefault('U', 0);
        int d = map.getOrDefault('D', 0);
        int r = map.getOrDefault('R', 0);
        int l = map.getOrDefault('L', 0);
        if(u == d && r == l) return true;
        return false;        
    }
}
```