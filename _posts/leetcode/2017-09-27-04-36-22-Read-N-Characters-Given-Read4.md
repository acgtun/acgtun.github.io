---
layout: post
title: Read N Characters Given Read4
date: 2017-09-27 04:36:22
categories: leetcode
---

```java
{{ % raw %}}
{{/* The read4 API is defined in the parent class Reader4.
      int read4(char[] buf); */

public class Solution extends Reader4 {
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    public int read(char[] buf, int n) {
        int k = 0;
        while(k < n) {
            char[] buffer = new char[4];
            int s = read4(buffer);
            for(int i = 0;i < s && k < n;++i) {
                buf[k++] = buffer[i];
            }
            if(s < 4) break;
        }

        return k;
    }
}

//////////
/* The read4 API is defined in the parent class Reader4.
      int read4(char[] buf); */

public class Solution extends Reader4 {
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    public int read(char[] buf, int n) {
        int index = 0;
        char[] cbuf = new char[4];
        while(index < n) {
            int size = read4(cbuf);
            for(int i = 0;i < size && index < n;++i) buf[index++] = cbuf[i];
            if(size < 4) return index;
        }
        return index;
    }
}
}}
{{ % endraw %}}
```