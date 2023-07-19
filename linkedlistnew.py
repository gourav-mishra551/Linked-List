class Node:
    def __init__(self, data = None , next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
     # insert in Linked List
    def insert_at_beginig(self, data):
        node = Node(data, self.head)
        self.head =node
    # Print linked list
    def print(self):
        if self.head is None:
            print("empty")
            return
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)
    # Insert at the end of linked list
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None) 
    
    # Inserting an Array
    def inster_values(self , data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    # Length of the Inserted linked list
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count
    
    # Removing at Specific Index
    def remove_at(self , index):
        if index<0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    # Inserting at given Index
    def insert_at(self , index , data):
        if index<0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_beginig(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
            itr = itr.next
            count += 1
        

if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_at_beginig(5)
    # ll.insert_at_beginig(89)
    # ll.insert_at_end(79)
    ll.inster_values(['g','m','o' , 'p'])
    ll.remove_at(2)
    ll.print()
