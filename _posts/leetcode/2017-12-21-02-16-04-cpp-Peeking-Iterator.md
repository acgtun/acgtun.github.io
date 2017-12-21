---
layout: post
title: Peeking Iterator
date: 2017-12-21 02:16:04
categories: leetcode
---

```cpp
// Below is the interface for Iterator, which is already defined for you.
// **DO NOT** modify the interface for Iterator.
class Iterator {
    struct Data;
	Data* data;
public:
	Iterator(const vector<int>& nums);
	Iterator(const Iterator& iter);
	virtual ~Iterator();
	// Returns the next element in the iteration.
	int next();
	// Returns true if the iteration has more elements.
	bool hasNext() const;
};


class PeekingIterator : public Iterator {
public:
	PeekingIterator(const vector<int>& nums) : Iterator(nums) {
	    // Initialize any member here.
	    // **DO NOT** save a copy of nums and manipulate it directly.
	    // You should only use the Iterator interface methods.
	    flag = true;
	    if(Iterator::hasNext()) {
	        val = Iterator::next();
	        flag = false;
	    }
	}

    // Returns the next element in the iteration without advancing the iterator.
	int peek() {
        return val;
	}

	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	int next() {
	    int ret = val;
	    if(Iterator::hasNext()) {
	        val = Iterator::next();
	        flag = false;
	    } else {
	        flag = true;
	    }
	    
	    return ret;
	}

	bool hasNext() const {
	    return flag == false;
	}
	
	int val;
	bool flag;
};
```