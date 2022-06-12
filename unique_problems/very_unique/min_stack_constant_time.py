class MinStack:

    def __init__(self):
        self.arr = []
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        

    def pop(self) -> None:
        return self.arr.pop(-1)
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return sorted(self.arr)[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

###IMPROVED VERSION#######
class MinStack:

    def __init__(self):
        self.arr = []
        # self.mini = float("inf")
        

    def push(self, val: int) -> None:
        if(len(self.arr)==0):
            self.arr.append([val,val])
        elif(val<self.arr[-1][1]):
            self.arr.append([val,val])
        else:
            self.arr.append([val,self.arr[-1][1]])
        

    def pop(self) -> None:
        self.arr.pop(-1)
        # return item[0]
        

    def top(self) -> int:
        return self.arr[-1][0]
        

    def getMin(self) -> int:
        return self.arr[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()