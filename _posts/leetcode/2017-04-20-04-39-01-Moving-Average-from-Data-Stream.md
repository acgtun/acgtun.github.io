---
layout: post
title: Moving Average from Data Stream
date: 2017-04-20 04:39:01
categories: leetcode
---

```java
{{ % raw %}}
{{public class MovingAverage {

    /** Initialize your data structure here. */
    private int windowSize;
    double sum = 0;
    Queue<Integer> q = new LinkedList<>(); 
    
    public MovingAverage(int size) {
        windowSize = size;    
    }
    
    public double next(int val) {
        if(q.size() >= windowSize) {
            int f = q.remove();
            sum -= f;
        }
        q.add(val);
        sum += val;
        
        return sum / q.size();
    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.next(val);
 */
}}
{{ % endraw %}}
```