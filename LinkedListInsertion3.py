class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        head = None

    def printList(self):
        # 1. make temporary node as head
        temp = self.head
        # 2. loop till temp is NULL
        while temp:
            print(temp.data)
            temp = temp.next

    # time complexity = O(1)
    def insertAtBeginning(self, new_data):
        # 1. creating new node
        newNode = Node(new_data)
        # 2. pointing new node next ptr to the first element
        newNode.next = self.head
        # 3. making new node as head
        self.head = newNode

    # inserting at middle if the data is integer

    def insertAtMiddle(self, new_data):
        newNode = Node(new_data)
        temp = self.head
        while temp.data < new_data:
            prev = temp
            temp = temp.next
        newNode.next = temp
        prev.next = newNode

    # time complextiy  is O(n)
    def insertAfter(self, prev_node_data, new_data):
        temp = self.head
        # finding the previous node
        while(temp.data != prev_node_data):
            temp = temp.next
        # 1. create a new Node
        new_node = Node(new_data)
        # 2. point the next pointer of new Node to the next node of previous node
        new_node.next = temp.next
        # 3. point the next pointer of previous node to the new Node
        temp.next = new_node
    # time complexity is O(n)

    def append(self, new_data):
        # 1. create a new node
        new_node = Node(new_data)
        # 2. if head is empty make new node as head
        if self.head is None:
            self.head = new_node
            return
        # 3. make temporary node as head and traverse through linked list and make last node as temp node
        temp = self.head
        while(temp.next):
            temp = temp.next
        # 4. point next ptr of temporary node to new Node
        temp.next = new_node


if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(4)
    llist.head.next = second
    second.next = third
    llist.append(7)
    llist.printList()
