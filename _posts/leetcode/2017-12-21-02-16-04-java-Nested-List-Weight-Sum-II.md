---
layout: post
title: Nested List Weight Sum II
date: 2017-12-21 02:16:04
categories: leetcode
---

```java
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *     // Constructor initializes an empty nested list.
 *     public NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     public NestedInteger(int value);
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // Set this NestedInteger to hold a single integer.
 *     public void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     public void add(NestedInteger ni);
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
public class Solution {
    public static class Pair {
        int first;
        int second;
    
        public Pair(int _first, int _second) {
            first = _first;
            second = _second;
        }
        
        public int getFirst() {
            return first;
        }
        
        public int getSecond() {
            return second;
        }
    }
    
    ArrayList<Pair> value = new ArrayList<Pair>();
    int max_depth = 0;
    
    private void depth_helper(List<NestedInteger> nestedList, int depth) {
        if(depth > max_depth) max_depth = depth;
        
        for(NestedInteger list : nestedList) {
            if(list.isInteger()) {
                value.add(new Pair(list.getInteger().intValue(), depth));
            } else {
                depth_helper(list.getList(), depth + 1);
            }
        }
    }
    
    public int depthSumInverse(List<NestedInteger> nestedList) {
        depth_helper(nestedList, 1);
        int sum = 0;
        for(int i = 0;i < value.size();i++) {
            sum += value.get(i).getFirst() * (max_depth - value.get(i).getSecond() + 1);
        }
        
        return sum;
    }
}
```