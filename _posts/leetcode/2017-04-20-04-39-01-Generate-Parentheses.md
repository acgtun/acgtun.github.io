---
layout: post
title: Generate Parentheses
date: 2017-04-20 04:39:01
categories: leetcode
---

```java
{{ % raw %}}
{{public class Solution {
    List<String> res = new ArrayList<>();
    private void dfs(int l, int r, int n, char[] cur) {
        if(r == n) {
            res.add(new String(cur));
            return ;
        }
        if(l > r) {
            cur[l + r] = ')';
            dfs(l, r + 1, n, cur);
            
            if(l < n) {
                cur[l + r] = '(';
                dfs(l + 1, r, n, cur);
            }
        } else { // l == r
            cur[l + r] = '(';
            dfs(l + 1, r, n, cur);
        }
    }
    
    public List<String> generateParenthesis(int n) {
        if(n == 0) {
            return res;
        }
        char[] cur = new char[2 * n];
        dfs(0, 0, n, cur);
        return res;
    }
}
}}
{{ % endraw %}}
```