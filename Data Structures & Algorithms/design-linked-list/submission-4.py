class ListNode:
    def __init__(self, val=0, nxt=None, prv=None):
        self.val = val
        self.next = nxt ##NONE NOT NEXT
        self.prev = prv ##NONE NOT PREV


class MyLinkedList:
    
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        ##basic 2 node system
        self.head.next = self.tail 
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index<0 or index>=self.size:
            return -1
        curr = self.head 
        for i in range(index+1): ## because list is 0-idex
            curr = curr.next
        return curr.val
            

    def addAtHead(self, val: int) -> None:
        curr  = self.head 
        new_node = ListNode(val)
        after = curr.next

        curr.next = new_node
        new_node.next = after
        after.prev = new_node
        new_node.prev = curr 
        self.size += 1

        
    def addAtTail(self, val: int) -> None:
        last = self.tail 
        new_node = ListNode(val)
        penultimate = last.prev 
        penultimate.next = new_node
        new_node.next = last
        new_node.prev = penultimate
        last.prev = new_node
        self.size +=1

        

    def addAtIndex(self, index: int, val: int) -> None:
        #split by case 
        if index<0:
            index = 0
        if index>self.size:
            return None
        if index == self.size: #aka adding at the end
            self.addAtTail(val)
            return

        curr = self.head
        for i in range(index):
            curr = curr.next 

        new_node = ListNode(val)
        after = curr.next 
        curr.next = new_node
        new_node.prev = curr 
        new_node.next = after 
        after.prev = new_node
        self.size +=1



    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return None ##since its an invalid index all together

        curr = self.head
        for i in range(index + 1):
            curr = curr.next
        AfterOld = curr.next
        BeforeOld = curr.prev
        BeforeOld.next = AfterOld
        AfterOld.prev = BeforeOld
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)