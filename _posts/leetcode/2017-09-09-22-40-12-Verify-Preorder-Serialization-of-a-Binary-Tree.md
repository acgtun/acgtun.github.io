---
layout: post
title: Verify Preorder Serialization of a Binary Tree
date: 2017-09-09 22:40:12
categories: leetcode
---

```java
{{ % raw %}}
{{class Solution {
    private boolean deserialize(Queue<String> q) {
        if(q.isEmpty()) return false;
        
        if(q.poll().equals("#")) return true;
        else {
            if(!deserialize(q)) return false;
            if(!deserialize(q)) return false;
            return true;
        }
    }
    
    public boolean isValidSerialization(String preorder) {
        String[] nodes = preorder.split(",");
        Queue<String> q = new LinkedList<>();
        for(int i = 0;i < nodes.length;++i) {
            q.add(nodes[i]);
        }
        return deserialize(q) && q.size() == 0;
    }
}
}}
{{ % endraw %}}
```