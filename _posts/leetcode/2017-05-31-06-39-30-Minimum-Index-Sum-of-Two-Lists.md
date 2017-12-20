---
layout: post
title: Minimum Index Sum of Two Lists
date: 2017-05-31 06:39:30
categories: leetcode
---

```java
{{ % raw %}}
{{public class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        ArrayList<String> ret = new ArrayList<>();
        int minSum = Integer.MAX_VALUE;
        for(int i = 0;i < list1.length;++i) {
            for(int j = 0;j < list2.length;++j) {
                if(list1[i].equals(list2[j])) {
                    if(i + j < minSum) {
                        minSum = i + j;
                        ret.clear();
                        ret.add(list1[i]);
                    } else if(i + j == minSum) {
                        ret.add(list1[i]);
                    }    
                }
            }
        }

        String[] ans = new String[ret.size()];
        for(int i = 0;i < ret.size();++i) {
            ans[i] = ret.get(i);
        }
        return ans;
    }
}
}}
{{ % endraw %}}
```