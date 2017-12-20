---
layout: post
title: Read N Characters Given Read4 II - Call multiple times
date: 2017-04-20 04:39:01
categories: leetcode
---

```cpp
{{ % raw %}}
{{// Forward declaration of the read4 API.
int read4(char *buf);

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    
    char chr[5];
    int chrindex;
    int chrsize;
    
    bool end_of_file;
    
    Solution() {
        chrsize = 0;
        chrindex = 0;
        end_of_file = false;
    }
    
    int read(char *buf, int n) {
        int cl = 0;
        while(cl < n) {
            if(chrindex < chrsize) {
                buf[cl++] = chr[chrindex++];
            } else if(end_of_file == false) {
                chrsize = read4(chr);
                if(chrsize < 4) {
                    end_of_file = true;
                }
                chrindex = 0;
            } else {
                break;
            }
        }
        
        return cl;
    }
};
}}
{{ % endraw %}}
```