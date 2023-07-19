#linked list is a form of a sequential collection and it does not have to be in order. A linked list is made up of independent nodes that may contain any type of node that may contain any type of data and each node has a reference to the next node in the link.
# A node store the refernece of the next node in the linked list so the tail has null reference .
# types of linked list are 1 single linked list 2 circular linked list 3 double linked list 4 circular doubly linked list 

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    # insert in Linked List
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    # Traverse Singly Linked List
    
    def traverseList(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

 # Search for a node in Singly Linked List
    def searchSLL(self, nodeValue):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The node does not exist in this SLL"
    # Delete a node from Singly Linked List
    def deleteNode(self, location):
        if self.head is None:
            return "The Singly Linked List does not exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    # Delete entire SLL
    def deleteEntireSLL(self):
        if self.head is None:
            print("SLL does not exist")
        else:
            self.head = None
            self.tail = None

singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(44,6)
print([node.value for node in singlyLinkedList]) 

# node1 = Node(1)
# node2 = Node(2)

# singlyLinkedList.head = node1
# singlyLinkedList.head.next = node2
# singlyLinkedList.tail = node2

singlyLinkedList.insertSLL(3,1)
singlyLinkedList.insertSLL(4,1)
print([node.value for node in singlyLinkedList]) 
singlyLinkedList.insertSLL(5,3)
print([node.value for node in singlyLinkedList]) 

#for input in linked list
# if inserstion at the begning of the list 
# 1. node.next = head(head ka jo reference tha use node ka reference bana do)  2. head= node (head ke reference mai node ka(pointer) reference dal do)

# if inserstion at the end of the list
#node.next = null (list mai akhiri value ka refrence null hota hai) last.next = node (last element jo tha uske next yani refrence ko node ke reference ) tail = node (ab tail ko node se connect kr do refence daal kr)

#if inserstion is in the middle of the linked list 
#find location(loop) 2. current.next = node( jo element find kra uske reference mai node ka reference daal do) 3 node.next = nextnode (node ke reference mai agle node ka reference daal do)