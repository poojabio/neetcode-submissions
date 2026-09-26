class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.array = [None] * capacity 

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        self.array[self.length] = n ##final pos insertion
        self.length += 1

    def popback(self) -> int:
        self.length -=1
        val = self.array[self.length]
        self.array[self.length] = None
        return val
 
    def resize(self) -> None:
        self.capacity *=  2
        copy_array = [None] * self.capacity
        for value in range(self.length):
            copy_array[value] = self.array[value]
        self.array = copy_array

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
