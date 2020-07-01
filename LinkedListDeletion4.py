class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def deleteNode(self, key):
        temp = self.head
        # if key was not present in the linked LinkedList
        if temp == None:
            return
        # if head node itself holds the key to be deleted
        if(temp.data == key):
            self.head = temp.next
            temp = None
            return
        # search for the key to be deleted and keep track of previous node
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # unlink the node from the linked LinkedList
        prev.next = temp.next
        temp = None


if __name__ == "__main__":
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)
    llist.append(5)
    llist.deleteNode(5)
    llist.printList()
