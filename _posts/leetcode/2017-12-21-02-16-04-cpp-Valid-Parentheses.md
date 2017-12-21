---
layout: post
title: Valid Parentheses
date: 2017-12-21 02:16:04
categories: leetcode
---

```cpp
class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for(size_t i = 0;i < s.size();++i) {
            if(s[i] == '(' || s[i] == '[' || s[i] == '{') {
                st.push(s[i]);
            } else if(s[i] == ')' || s[i] == ']' || s[i] == '}') {
                if(st.empty()) {
                    return false;
                }
                
                if(s[i] == ')' && st.top() != '(') {
                    return false;
                }
                
                if(s[i] == ']' && st.top() != '[') {
                    return false;
                }
                
                if(s[i] == '}' && st.top() != '{') {
                    return false;
                }
                
                st.pop();
            }
        }
        
        return st.empty();
    }
};
```