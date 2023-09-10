# creating a Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # this method is called to make our linkedlist iterable.
    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next


class Queue:
    def __init__(self):
        self.linkedList = LinkedList()
    
    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)
    
    def enQueue(self, value):
        newNode = Node(value)
        # if the linkedlist is empty
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        
        else:
            # we know that tail points to the last node of the linkedlist. so we made the tail(previous last node) to point at the element we're enqueuing and then in the second line we had our tail point to it since it is our new last element
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode

    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False
    
    def deQueue(self):
        if self.linkedList.head == None:
            print('Queue empty')
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode

    def peek(self):
        '''
        returns the value of head
        '''
        if self.isEmpty():
            print('The Queue is empty')
        else:
            return self.linkedList.head


# custQueue = Queue()
# custQueue.enQueue(5)
# custQueue.enQueue(4)
# # custQueue.enQueue('klsjfks')
# custQueue.enQueue(9)
# custQueue.enQueue(0)
# custQueue.enQueue(8)
# custQueue.deQueue()
# print(custQueue.peek())
# print(custQueue)