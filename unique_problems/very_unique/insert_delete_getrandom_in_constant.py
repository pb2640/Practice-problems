# class RandomizedSet:

#     def __init__(self):
#         self.arr = collections.deque([])
#         self.hashmap = {}
#         self.rotations = 0
#         self.position = 0


#     def insert(self, val: int) -> bool:
#         if(val in self.hashmap):
#             #if item in set do nothing
#             return False
#         else:
#             #add item and return false
#             #in case of insufficient
#             if(self.position<len(self.arr)):
#                 self.arr[self.position] = val
#             else:
#                 self.arr.append(val)
#             #{val : index}
#             self.hashmap[val] = self.position
#             self.position+=1
#             return True


#     def remove(self, val: int) -> bool:
#         if(val in self.hashmap):
#             replace = self.arr[-1]
#             pos = self.hashmap[val]-self.rotations
#             self.arr[pos] = replace
#             self.position-=1
#             self.hashmap.pop(val)
#             return True
#         else:
#             return False


#     def getRandom(self) -> int:
#         ele = self.arr.popleft()
#         self.arr.append(ele)
#         self.rotations+=1
#         return ele


###################
# BETTER WAY
###################

from random import choice


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            # move the last element to the place idx of the element to delete
            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_element] = last_element, idx
            # delete the last element
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)
