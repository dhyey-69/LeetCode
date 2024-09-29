# 432. All O`one Data Structure

# Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

# Implement the AllOne class:

# AllOne() Initializes the object of the data structure.
# inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
# dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
# getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
# getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
# Note that each function must run in O(1) average time complexity.

 

# Example 1:

# Input
# ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
# [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
# Output
# [null, null, null, "hello", "hello", null, "hello", "leet"]

# Explanation
# AllOne allOne = new AllOne();
# allOne.inc("hello");
# allOne.inc("hello");
# allOne.getMaxKey(); // return "hello"
# allOne.getMinKey(); // return "hello"
# allOne.inc("leet");
# allOne.getMaxKey(); // return "hello"
# allOne.getMinKey(); // return "leet"

class AllOne:

    def __init__(self):
        self.key_count = {}
        self.count_keys = {}
        self.min_count = float('inf')
        self.max_count = float('-inf')

    def inc(self, key: str) -> None:
        if key in self.key_count:
            count = self.key_count[key]
            self.count_keys[count].remove(key)
            if not self.count_keys[count]:
                del self.count_keys[count]
            self.key_count[key] += 1
            new_count = count + 1
        else:
            self.key_count[key] = 1
            new_count = 1

        if new_count not in self.count_keys:
            self.count_keys[new_count] = set()
        self.count_keys[new_count].add(key)

        self.min_count = min(self.min_count, new_count)
        self.max_count = max(self.max_count, new_count)
        
        if new_count == 1:
            self.min_count = 1
        
        if self.min_count not in self.count_keys:
            self.min_count = min(self.count_keys.keys())

    def dec(self, key: str) -> None:
        if key not in self.key_count:
            return
        
        count = self.key_count[key]
        self.count_keys[count].remove(key)
        if not self.count_keys[count]:
            del self.count_keys[count]
        
        if count == 1:
            del self.key_count[key]
        else:
            self.key_count[key] -= 1
            new_count = count - 1
            if new_count not in self.count_keys:
                self.count_keys[new_count] = set()
            self.count_keys[new_count].add(key)

        if not self.count_keys:
            self.min_count = float('inf')
            self.max_count = float('-inf')
        else:
            if count == self.min_count and count not in self.count_keys:
                self.min_count = min(self.count_keys.keys())
            if count == self.max_count and count not in self.count_keys:
                self.max_count = max(self.count_keys.keys())

    def getMaxKey(self) -> str:
        if not self.key_count:
            return ""
        return next(iter(self.count_keys[self.max_count]))

    def getMinKey(self) -> str:
        if not self.key_count:
            return ""
        return next(iter(self.count_keys[self.min_count]))

# Your AllOne object will be instantiated and called as such:
obj = AllOne()
obj.inc("hello")
obj.inc("hello")
# obj.dec("hello")
obj.dec("world")
param_3 = obj.getMaxKey()
param_4 = obj.getMinKey()
print(param_3)
print(param_4)