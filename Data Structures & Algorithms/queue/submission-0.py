class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None
        
class Deque:
    
    def __init__(self):
        self.head = Node() 
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0 

    def append(self, value: int) -> None:
        prior = self.tail.prev
        new_node = Node(value)
        prior.next = new_node
        new_node.next = self.tail 
        self.tail.prev = new_node 
        new_node.prev = prior
        self.size +=1 


    def appendleft(self, value: int) -> None:
        old_first = self.head.next 
        new_node = Node(value)
        self.head.next = new_node
        new_node.next = old_first
        old_first.prev = new_node
        new_node.prev = self.head 
        self.size +=1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        else:
            to_rmv = self.tail.prev 
            val = to_rmv.val
            old = to_rmv.prev
            old.next = self.tail
            self.tail.prev = old
            self.size -= 1
            return val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        else:
            to_rmv = self.head.next 
            val = to_rmv.val
            self.head.next = to_rmv.next
            to_rmv.next.prev = self.head 
            self.size -= 1
            return val

        
