---
layout: post
title: Read N Characters Given Read4
date: 2017-12-12 18:33:48
categories: leetcode
---

```cpp
// Forward declaration of the read4 API.
int read4(char *buf);

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    int read(char *buf, int n) {
        char chr[5];
        int cl = 0;
        while(cl < n) {
            int l = read4(chr);
            for(int i = 0;i < l && cl < n;++i) {
                buf[cl++] = chr[i];
            }
            if(l < 4) break;
        }
        
        return cl;
    }
};
```