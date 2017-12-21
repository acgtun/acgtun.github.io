---
layout: post
title: Longest Common Prefix
date: 2017-12-21 02:16:04
categories: leetcode
---

```java
public class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs.length == 0) return "";
        StringBuilder res = new StringBuilder();
        int index = 0;
        while(true) {
            if(strs[0].length() == index) {
                return res.toString();
            }
            char c = strs[0].charAt(index);
            for(int i = 1;i < strs.length;++i) {
                if(strs[i].length() == index) {
                    return res.toString();
                }
                if(strs[i].charAt(index) != c) {
                    return res.toString();
                }
            }
            res.append(c);
            index++;
        }
    }
}
```