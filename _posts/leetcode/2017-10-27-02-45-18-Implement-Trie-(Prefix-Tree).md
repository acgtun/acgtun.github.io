---
layout: post
title: Implement Trie (Prefix Tree)
date: 2017-10-27 02:45:18
categories: leetcode
---

```java
{{ % raw %}}
{{public class Trie {
    private class TrieNode {
        public TrieNode() {
            children = new TrieNode[26];
            isWord = false;
        }
        
        TrieNode[] children;
        boolean isWord;
    }

    TrieNode root;
    
    /** Initialize your data structure here. */
    public Trie() {
        root = new TrieNode();    
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        TrieNode p = root;
        for(int i = 0;i < word.length();++i) {
            char c = word.charAt(i);
            if(p.children[c - 'a'] == null) {
                p.children[c - 'a'] = new TrieNode();
            }
            p = p.children[c - 'a'];
        }
        p.isWord = true;
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        TrieNode p = root;
        for(int i = 0;i < word.length();++i) {
            char c = word.charAt(i);
            if(p.children[c - 'a'] != null) {
                p = p.children[c - 'a'];
            } else {
                return false;
            }
        }
        
        return p.isWord;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        TrieNode p = root;
        for(int i = 0;i < prefix.length();++i) {
            char c = prefix.charAt(i);
            if(p.children[c - 'a'] != null) {
                p = p.children[c - 'a'];
            } else {
                return false;
            }
        }
        
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
}}
{{ % endraw %}}
```