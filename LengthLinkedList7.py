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
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def printList(self):
        current_node = self.head
        if current_node is None:
            return
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    # finding length of linked list iteratively
    def count_length(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    # finding length of linked list recursively
    def count_length_recursively(self, node):
        current_node = node
        if current_node is None:
            return 0
        else:
            return 1+self.count_length_recursively(current_node.next)

    def get_count(self):
        return self.count_length_recursively(self.head)


if __name__ == "__main__":
    llist = LinkedList()
    llist.append('A')
    llist.append('B')
    llist.append('C')
    llist.append('D')
    llist.append('E')
    llist.printList()
    print(llist.count_length())
    print(llist.get_count())
