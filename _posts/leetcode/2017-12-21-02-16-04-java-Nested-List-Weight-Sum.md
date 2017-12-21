---
layout: post
title: Nested List Weight Sum
date: 2017-12-21 02:16:04
categories: leetcode
---

```java
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
public class Solution {
    public int depthSum(List<NestedInteger> nestedList, int depth) {
        int sum = 0;
        for(NestedInteger list : nestedList) {
            if(list.isInteger()) sum += list.getInteger() * depth;
            else {
                sum += depthSum(list.getList(), depth + 1); 
            }
        }
        
        return sum;
    }
    public int depthSum(List<NestedInteger> nestedList) {
        return depthSum(nestedList, 1);    
    }
}
```