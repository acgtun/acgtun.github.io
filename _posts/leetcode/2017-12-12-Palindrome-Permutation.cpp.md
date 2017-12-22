---
layout: post
title: Palindrome Permutation
date: 2017-12-12 18:33:48
categories: leetcode
---

```cpp
class Solution {
public:
    bool canPermutePalindrome(string s) {
        unordered_map<char, int> count;
        for(size_t i = 0;i < s.size();++i) {
            count[s[i]]++;
        }
        
        int c = 0;
        for(unordered_map<char,int>::iterator it = count.begin(); it != count.end();++it) {
            if(it->second % 2 == 1) c++;
        }
        
        if(c > 1) return false;
        return true;
    }
};
```