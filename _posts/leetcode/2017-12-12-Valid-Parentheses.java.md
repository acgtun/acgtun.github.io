---
layout: post
title: Valid Parentheses
date: 2017-12-12 18:33:48
categories: leetcode
---

```java
public class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<>();
        for(int i = 0;i < s.length();++i) {
            char c = s.charAt(i);
            if(c == '(' || c == '[' || c == '{') {
                st.push(c);
            } else {
                if(st.empty()) return false;
                char t = st.pop().charValue();
                if(t == '[' && c == ']') {continue;}
                if(t == '{' && c == '}') {continue;}
                if(t == '(' && c == ')') {continue;}
               
                return false;
                
            }
        }
        if(st.empty()) return true;
        return false;
    }
}
```